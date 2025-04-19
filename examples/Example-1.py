
from delegent.core.engines.assignment_engine import RoleBasedAssignmentEngine
from delegent.core.engines.planner import TaskPlanner
from delegent.core.agents.agent import Agent
from delegent.core.tasks.task import Task
from delegent.core.tasks.subtask import Subtask
from user_config import AGENT_PROFILES


# """
# Step 1: Define the complex task
task = Task(id='T200', desc='Create a product launch document')

# Step 2: Define Agents - Objects of Agent class
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

