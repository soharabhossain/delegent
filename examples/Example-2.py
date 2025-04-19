
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

