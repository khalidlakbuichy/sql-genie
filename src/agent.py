import os
import pandas as pd
from dotenv import load_dotenv
from langchain_community.utilities import SQLDatabase
from langchain_openai import ChatOpenAI
from langchain_community.agent_toolkits import create_sql_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough

load_dotenv()

class SQLAgent:
    def __init__(self, db_path="northwind.db"):
        self.db = SQLDatabase.from_uri(f"sqlite:///{db_path}")
        self.llm = ChatOpenAI(model="gpt-4", temperature=0)
        
        self.agent_executor = create_sql_agent(
            llm=self.llm,
            db=self.db,
            agent_type="openai-tools",
            verbose=True
        )
        
        template = """You are a SQLite expert. Write a SQL query to answer this question.

Return only the SQL query, no explanation or markdown.

Schema:
{schema}

Question: {question}"""
        
        prompt = ChatPromptTemplate.from_template(template)
        
        self.sql_chain = (
            RunnablePassthrough.assign(schema=lambda _: self.db.get_table_info())
            | prompt
            | self.llm
            | StrOutputParser()
        )

    def ask(self, question):
        """Get a text answer by querying the database."""
        try:
            response = self.agent_executor.invoke(question)
            return response['output']
        except Exception as e:
            return f"Error: {e}"

    def get_data(self, question):
        """Generate SQL and return the result as a DataFrame."""
        try:
            sql_query = self.sql_chain.invoke({"question": question})
            sql_query = sql_query.strip().replace("```sql", "").replace("```", "").strip()
            
            df = pd.read_sql_query(sql_query, self.db._engine)
            return df, sql_query
        except Exception as e:
            print(f"Error: {e}")
            return None, None

    def generate_chart_code(self, df, question):
        """Generate Plotly code for visualizing the data."""
        columns = ", ".join(df.columns.tolist())
        sample = df.head(2).to_dict()
        
        prompt = f"""Write a single line of Plotly code to visualize this data.

Question: {question}
Columns: {columns}
Sample: {sample}

Use px.bar, px.line, px.pie, or px.scatter. The df is already loaded.
Return only the code line: fig = px..."""
        
        response = self.llm.invoke(prompt)
        return response.content.replace("```python", "").replace("```", "").strip()