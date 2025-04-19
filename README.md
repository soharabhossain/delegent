
# Delegent

**Delegent** is a modular and extensible framework for intelligent **task decomposition** and **delegation** in **multi-agent workflows**. Designed to work with LLM-powered agents, Delegent empowers dynamic task routing, parallel execution, and outcome aggregation—enabling scalable agentic systems across diverse domains.

> ✨ The name *Delegent* blends "Delegate" + "Agent" — representing an agent that intelligently delegates responsibilities by decponsing a given task into multiple subtasks and assigning them to appropriate agents.

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

