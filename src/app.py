import streamlit as st
import pandas as pd
import plotly.express as px
from agent import SQLAgent

st.set_page_config(page_title="SQL Genie", page_icon="🧞", layout="wide")

if "agent" not in st.session_state:
    st.session_state.agent = SQLAgent()

if "messages" not in st.session_state:
    st.session_state.messages = []

st.title("SQL Genie")
st.markdown("Ask questions about your data.")

for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])

if prompt := st.chat_input("What would you like to know?"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)
    
    with st.chat_message("assistant"):
        response = st.session_state.agent.ask(prompt)
        st.write(response)
        
        try:
            df, sql = st.session_state.agent.get_data(prompt)
            
            if df is not None and not df.empty:
                st.dataframe(df, use_container_width=True)
                
                plot_code = st.session_state.agent.generate_chart_code(df, prompt)
                local_scope = {"df": df, "px": px}
                exec(plot_code, globals(), local_scope)
                
                if fig := local_scope.get("fig"):
                    st.plotly_chart(fig, use_container_width=True)
                    
        except Exception as e:
            st.warning(f"Could not generate visualization: {e}")
        
        st.session_state.messages.append({"role": "assistant", "content": response})