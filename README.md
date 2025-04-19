
# Delegent

**Delegent** is a modular and extensible framework for intelligent **task decomposition** and **delegation** in **multi-agent workflows**. Designed to work with LLM-powered agents, Delegent empowers dynamic task routing, parallel execution, and outcome aggregation—enabling scalable agentic systems across diverse domains.

✨ The name *Delegent* blends "Delegate" + "Agent" — representing an agent that intelligently delegates responsibilities by decponsing a given task into multiple subtasks and assigning them to appropriate agents.

---

## 🚀 Features

- 🔨 **Task Decomposition Engine** – Breaks down high-level goals into sub-tasks using LLMs or rule-based logic.
- 🤖 **Agent-Oriented Delegation** – Assigns tasks to the most suitable agents based on skill, priority, or load.
- 🔄 **Workflow Orchestration** – Manages execution, context sharing, and inter-agent communication.
- 📦 **Modular Design** – Easily plug in custom agents, tools, or LLM backends (OpenAI, Groq, Claude, etc.).
- 📊 **Result Aggregation** – Gathers and evaluates outputs from agents to deliver a unified result.

---

## 🧩 Use Cases

- AI-powered research assistants
- Business process automation
- Code and data analysis pipelines
- Multi-tool developer agents
- Conversational task managers

---

## 📁 Project Structure

```bash
delegent/
├── core/                 # Task parser, decomposer, and delegation logic
        |-- agents
        |-- engines
        |-- evaluator
        |-- execution
        |-- tasks

├── data/                 # Agent registry and definitions
├── llm/                  # Definitions of LLM providers
├── test/                 # Test code
├── utils/                # Utility functions, loader, logger, etc.
├── workflows/            # Sample workflows and task pipelines (to be added)
├── config.py             # config for logging
├── .env                  # Environment variables (e.g., API keys) & LLM configuration
├── requirements.txt      # Dependencies
├── examples/             # Example usage scripts
└── README.md


```

## ⚙️ Installation

```bash

git clone https://github.com/soharabhossain/delegent.git
cd delegent
pip install -r requirements.txt

```

## 🔧 Usage
```bash
from delegent.core.decomposer import TaskDecomposer
from delegent.core.delegator import TaskDelegator
from delegent.agents.registry import AgentRegistry

# Step 1: Initialize task
goal = "Summarize the latest AI trends and generate a report with visualizations."

# Step 2: Decompose
subtasks = TaskDecomposer().decompose(goal)

# Step 3: Delegate
delegator = TaskDelegator(AgentRegistry())
results = delegator.delegate(subtasks)

# Step 4: Aggregate
final_output = delegator.aggregate(results)
print(final_output)
```


## 🔌 Supported LLMs & Tools
- OpenAI GPT-4 / GPT-3.5
- Claude, Gemini (via API)
- Custom tool usage via Tool Calling or Function APIs
- Web search, code execution, PDF parsing, and more (plugin-ready)


## 📚 Documentation
- Coming soon! In the meantime, explore:
 > examples/ folder
 > Source code docstrings
 > Issues and Discussions tab for Q&A


## 🧠 Credits 
 - Delegent is developed and maintained by Dr. Soharab Hossain Shaikh, Associate Professor, AI Researcher and Enthusiast.


## 📜 License
### MIT License. See LICENSE for details.

## ⭐️ Contribute
 - Pull requests, feature suggestions, and feedback are welcome!
 - Please open an issue or join the discussions to get started.

