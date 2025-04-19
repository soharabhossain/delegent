
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

├── workspace             # User workspace
             ├── agents   # User's agent profiles and registry
             ├── config   # User's logging configuration settings/preference
             ├── log      # Path to the log file            
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
```
- Create a virtual environment
```bash
python -m venv venv
```
- Activate the virtual environment
```bash
venv/Scripts/activate
```
```bash
pip install -r requirements.txt

```

## 🔧 Usage
```bash
from delegent.core.engines.assignment_engine import RoleBasedAssignmentEngine
from delegent.core.engines.planner import TaskPlanner
from delegent.core.agents.agent import Agent
from delegent.core.tasks.task import Task
from delegent.core.tasks.subtask import Subtask
from user_config import AGENT_PROFILES


# Step 1: Define the complex task
task = Task(id='T200', desc='Create a product launch document')

# Agents - Objects of Agent class
agents = [Agent.from_dict(profile) for profile in AGENT_PROFILES]
print(agents)

# Step 3: Initialize planner and assignment engine
planner = TaskPlanner()
assignment_engine = RoleBasedAssignmentEngine()

# Step 4: Decompose task into subtasks using the planner
subtasks = planner.decompose(task)

# Step 5: Schedule and assign
scheduled_subtasks = planner.schedule(subtasks)
assignments = assignment_engine.assign(scheduled_subtasks, agents)
planner.coordinate(assignments)

# Step 6: Output assignments
print("\nFinal Assignments:")
for sid, aid in assignments.items():
    print(f"Subtask {sid} -> Agent {aid if aid else 'Unassigned'}")

```

```bash

# Task Decomposition and Assignment
from delegent.core.tasks.task import Task
from delegent.core.agents.agent import Agent 
from user_config import AGENT_PROFILES
from delegent.core.tasks.llm_task_decomposer import LLMTaskDecomposer
from delegent.core.engines.assignment_engine import RoleBasedAssignmentEngine
from delegent.utils.utils import print_agent_info, print_subtask_description

# Agents - Objects of Agent class
agents = [Agent.from_dict(profile) for profile in AGENT_PROFILES]
print(agents)

# Task
task = Task(id="T201", desc="Create a ipython notebook analyzing historical stock data, analyze and visualize the results")

# Decomposer
decomposer = LLMTaskDecomposer()
subtasks = decomposer.decompose(task, [a.to_dict() for a in agents])

print("\n\n" + Fore.CYAN + Style.BRIGHT + "Task Decomposition:")
for stask in subtasks:
    print( Fore.GREEN + Style.BRIGHT + "Subtask: {}".format(stask))

# Assignment - assigning subtasks to individual agents
engine = RoleBasedAssignmentEngine()
assignments = engine.assign(subtasks, agents)

# Output - Subtask to Agent mapping
print("\n" + Fore.CYAN + Style.BRIGHT + "Final Assignments:")
for tid, aid in assignments.items():
    print(Fore.MAGENTA + Style.BRIGHT + f"{print_subtask_description(tid, subtasks)}")
    print(Fore.BLUE + Style.BRIGHT + f" ==> {print_agent_info(aid, agents)}" )

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

