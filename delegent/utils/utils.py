from delegent.core.agents.agent import Agent
from delegent.core.tasks.subtask import Subtask
from typing import List

# Function to print role and skills for a given agent ID
def print_agent_info(agent_id: str, agents: List[Agent]):
    for agent in agents:
        if agent.id == agent_id:
            # print(f"Agent ID: {agent.id}")
            # print(f"Role: {agent.role}")
            # print(f"Skills: {', '.join(agent.skills)}")
            output = f"Agent ID: {agent.id} " + f"Role: {agent.role} " + f"Skills: {', '.join(agent.skills)}"
            return output
    print(f"No agent found with ID: {agent_id}")


# Function to print subtask description for a given subtask ID
def print_subtask_description(subtask_id: str, subtasks: List[Subtask]):
    for subtask in subtasks:
        if subtask.id == subtask_id:
            # print(f"Subtask ID: {subtask.id}")
            # print(f"Description: {subtask.desc}")
            output = f"Subtask ID: {subtask.id} " + f"Description: {subtask.desc}"
            return output
    print(f"No subtask found with ID: {subtask_id}")
