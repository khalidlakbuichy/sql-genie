# 🧞‍♂️ SQL-Genie  
### Autonomous AI Data Analyst • Text → SQL → Insights → Charts

> Ask questions in plain English.  
> Get validated SQL, real data, and interactive charts — **automatically**.

**SQL-Genie** is an **agentic AI system** that transforms natural language into actionable insights from SQL databases.  
Unlike traditional text-to-SQL tools, SQL-Genie behaves like a **self-correcting data analyst** that understands schemas, fixes its own mistakes, and visualizes results intelligently.

---

## 🧠 Why SQL-Genie?

Most LLM tools stop at generating SQL.

**SQL-Genie goes further**:

- ✅ Learns the database schema automatically  
- 🔁 Fixes invalid SQL without human help  
- 📊 Generates charts dynamically using Python & Plotly  
- 🧩 Maintains conversational context across questions  

It's not a chatbot.  
It's an **autonomous data analyst**.

---

## 🧪 Live Demo

```text
User: What are the top 5 countries by total sales?
SQL-Genie:
✔ Generated SQL
✔ Fixed a GROUP BY error
✔ Executed query
✔ Rendered a bar chart
```

📸 *Add a demo.gif here for maximum impact.*

---

## 🛠️ Tech Stack

- **Python** — Core language
- **LangChain** — Agentic orchestration (LCEL)
- **OpenAI** — LLM backbone
- **Streamlit** — Interactive UI
- **Plotly** — Dynamic visualization
- **SQLite** (included) — Sample database

---

## ✨ Key Features

### 🔍 Schema Intelligence
- Automatically inspects tables, columns, and relationships
- Works with any SQL database (SQLite included)

### 🛡️ Self-Healing SQL
- Detects SQL errors at runtime
- Rewrites broken queries using error feedback

### 🎨 Autonomous Visualization
- Detects data type (time-series, categorical, numerical)
- Generates Plotly charts dynamically
- No hardcoded charts or templates

### 🧠 Conversational Memory
Supports follow-up questions like:
- "Now filter that by USA"
- "Only show data from 2023"

### 🔒 Safe Code Execution
- Visualization code runs in a sandboxed local scope
- Prevents unsafe code execution

---

## 🏗️ System Architecture

Built using Modern LangChain (LCEL):

```
User Question
    ↓
Streamlit UI
    ↓
LLM SQL Agent
    ├─→ Schema Inspector
    ├─→ SQL Generator
    ├─→ Query Validator (with error feedback loop)
    ├─→ Query Executor
    └─→ Chart Generator (Plotly)
    ↓
Output: Chart + Explanation
```

---

## 🚀 Getting Started

### ✅ Prerequisites

- Python 3.10+
- OpenAI API Key

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/YOUR_USERNAME/sql-genie.git
cd sql-genie
```

### 2️⃣ Install Dependencies

Recommended: create and activate a Python virtual environment, then install requirements:

```bash
python -m venv .venv
# macOS / Linux
source .venv/bin/activate
# Windows (PowerShell)
.venv\Scripts\Activate.ps1

pip install -r requirements.txt
```

### 3️⃣ Environment Variables

Create a `.env` file in the project root with your OpenAI key:

```
OPENAI_API_KEY="sk-..."
```

Or set it in your shell:

**macOS / Linux:**
```bash
export OPENAI_API_KEY="sk-..."
```

**Windows (PowerShell):**
```powershell
setx OPENAI_API_KEY "sk-..."
```

### 4️⃣ Run the Application

```bash
streamlit run src/app.py
```

Open: http://localhost:8501

---

## 🧪 Example Questions

Using the included Chinook.sqlite database:

- "Show me the top 5 tracks by unit price."
- "List all albums by the artist AC/DC."
- "What are the top 5 countries by total sales? Show a bar chart."

---

## 📁 Project Structure

```
sql-genie/
├── src/
│   ├── app.py        # Streamlit UI & session handling
│   ├── agent.py      # Agentic logic (LCEL, SQL reasoning)
│   └── db_utils.py   # Database helpers
├── Chinook.sqlite    # Sample database
├── requirements.txt  # Dependencies
├── .env              # Environment variables (gitignored)
└── README.md
```

---

## 🧩 Roadmap

- [ ] PostgreSQL support
- [ ] MySQL support
- [ ] CSV / Parquet ingestion
- [ ] Dashboard export
- [ ] Multi-agent planning

---

## 🤝 Contributing

This project demonstrates Agentic AI Systems and modern LLM orchestration.

Contributions are welcome:
- New database backends
- Better visualization logic
- Performance improvements

**Fork → Build → PR 🚀**

---

## 📄 License

MIT License