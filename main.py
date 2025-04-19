from colorama import init, Fore, Style

# Initialize colorama (especially needed on Windows)
init(autoreset=True)

# ----------------------------------------------------------------------------------

from delegent.core.engines.assignment_engine import RoleBasedAssignmentEngine
from delegent.core.engines.planner import TaskPlanner
from delegent.core.agents.agent import Agent
from delegent.core.tasks.task import Task
from delegent.core.tasks.subtask import Subtask
from user_config import AGENT_PROFILES


# """
# Step 1: Define the complex task
task = Task(id='T200', desc='Create a product launch document')

# Step 2: Define available agents
# agents = [
#     Agent(id='a1', role='researcher', skills=['research', 'analysis']),
#     Agent(id='a2', role='writer', skills=['writing', 'storytelling']),
#     Agent(id='a3', role='designer', skills=['design', 'illustration']),
#     Agent(id='a4', role='editor', skills=['editing'])
# ]

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

# """
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

"""
# Step 1: Define the complex task
task = Task(id='T200', desc='Create a product launch document')

# 2. Decompose the task into raw dictionaries
subtask_dicts = task.decompose()

# 3. Convert the raw dictionaries into Subtask objects
subtasks = [Subtask.from_dict(d) for d in subtask_dicts]

# 4. Print each Subtask object to verify
print("Subtasks created from Task using from_dict:")
for st in subtasks:
    print(f"ID: {st.id}, Desc: {st.desc}, Skill: {st.skill}, Role: {st.role}, Priority: {st.priority}")

"""

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# """
# Task Decomposition and Assignment
from delegent.core.tasks.task import Task
from delegent.core.agents.agent import Agent 
from user_config import AGENT_PROFILES
from delegent.core.tasks.llm_task_decomposer import LLMTaskDecomposer
from delegent.core.engines.assignment_engine import RoleBasedAssignmentEngine
from delegent.utils.utils import print_agent_info, print_subtask_description

# agents = [
#     Agent(id="a1", role="researcher", skills=["research", "analysis"]),
#     Agent(id="a2", role="writer", skills=["writing", "storytelling"]),
#     Agent(id="a3", role="designer", skills=["design", "illustration"]),
#     Agent(id="a4", role="editor", skills=["editing"])
# ]

# Agents - Objects of Agent class
agents = [Agent.from_dict(profile) for profile in AGENT_PROFILES]
print(agents)

# Task
# task = Task(id="T300", desc="Develop and launch a new AI-powered mobile app")
# task = Task(id="T200", desc="Create a product launch document")
# task = Task(id="T500", desc="Create history lesson plan")
# task = Task(id="T2000", desc="Create a story book for children")
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

print("\n\n")

# """
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# """
# Agent Registry
from delegent.core.agents.agent import Agent
from delegent.core.agents.agent_registry import AgentRegistry

REGISTRY_FILE = "./workspace/agents/agent_registry.json"

# Load existing registry or create a new one
registry = AgentRegistry.load_from_file(REGISTRY_FILE)

# Register new agents if not already present
if not registry.get_agent_by_id("A1"):
    registry.register(Agent(id="A1", role="writer", skills=["writing", "editing"]))
    registry.register(Agent(id="A2", role="researcher", skills=["research"]))
    registry.register(Agent(id="A3", role="designer", skills=["design"]))
    registry.register(Agent(id="A4", role="editor", skills=["editing", "video editing"]))
    registry.save_to_file(REGISTRY_FILE)

agents = registry.get_all()

for agent in agents:
    print(agent)
"""

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# """
# Agent Execution Layer
from delegent.core.execution.execution_layer import AgentExecutionLayer
from delegent.core.agents.agent import Agent
from delegent.core.tasks.subtask import Subtask

# 1. Create mock agents
agents = [
    Agent(id="a1", role="writer", skills=["writing", "editing"]),
    Agent(id="a2", role="designer", skills=["design", "illustration"]),
]

# 2. Create mock subtasks
subtasks = [
    Subtask(id="t1", desc="Write blog post", skill="writing", role="writer"),
    Subtask(id="t2", desc="Design banner", skill="design", role="designer"),
    Subtask(id="t3", desc="Proofread article", skill="editing", role="editor"),
    Subtask(id="t4", desc="Develop software", skill="coding, programming", role="software developer")  # Should fail
]

# 3. Mock assignment dict: subtask_id -> agent_id
assignments = {
    "t1": "a1",  # Success
    "t2": "a2",  # Success
    "t3": "a1",  # Success
    "t4": "a1" #Fail (role mismatch)
}

# 4. Call execution layer
execution_layer = AgentExecutionLayer()
results = execution_layer.execute(subtasks=subtasks, agents=agents, assignments=assignments)

# 5. Print results
for result in results:
    print(f"SubTask ID: {result.subtask_id} -> Agent ID: {result.agent_id} -> Status: {result.status}")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# Evaluator
from colorama import init
init(autoreset=True)


from delegent.core.execution.execution_layer import ExecutionResult
from delegent.core.execution.execution_layer import AgentExecutionLayer
from delegent.core.evaluator.evaluator import ResultAggregator

# # Step 1: Execution results - taking it from the previous section in variable `results`

# Step 2: Instantiate the ResultAggregator class
aggregator = ResultAggregator()

# Step 3: Pass results to the ResultAggregator to get the summary
summary = aggregator.summarize_results(results)

# Optionally print or store the summary
print(f"\nSummary: {summary}")

# """

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# """
from delegent.utils.logger import get_logger

logger = get_logger(__name__)
logger.info("Task decomposition started.")
logger.warning("No matching agent found.")
logger.error("Execution failed for subtask T101_3")

# """
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
