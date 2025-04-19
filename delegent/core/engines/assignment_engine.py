
from abc import ABC, abstractmethod
from typing import List, Dict
import random
from delegent.core.agents.agent import Agent
from delegent.core.tasks.subtask import Subtask
from delegent.utils.logger import log_step


# Abstract Base Class for Assignment Engines
class AssignmentEngine(ABC):
    @abstractmethod
    def assign(self, subtasks: List[Subtask], agents: List[Agent]) -> Dict[str, str]:
        pass

# Random Assignment Strategy
class RandomAssignmentEngine(AssignmentEngine):
    def assign(self, subtasks: List[Subtask], agents: List[Agent]) -> Dict[str, str]:
        assignments = {}
        for subtask in subtasks:
            agent = random.choice(agents)
            assignments[subtask.id] = agent.id
        return assignments

# Role-Based Assignment Strategy
class RoleBasedAssignmentEngine(AssignmentEngine):
    @log_step("RoleBasedAssignment")
    def assign(self, subtasks: List[Subtask], agents: List[Agent]) -> Dict[str, str]:
        assignments = {}
        for subtask in subtasks:
            assigned = False
            for agent in agents:
                if subtask.skill in agent.skills and agent.role == subtask.role:
                    assignments[subtask.id] = agent.id
                    assigned = True
                    break
            if not assigned:
                assignments[subtask.id] = "no agent found"
        return assignments

# Greedy Assignment Strategy
class GreedyAssignmentEngine(AssignmentEngine):
    def assign(self, subtasks: List[Subtask], agents: List[Agent]) -> Dict[str, str]:
        assignments = {}
        subtasks_sorted = sorted(subtasks, key=lambda x: x.priority or 0, reverse=True)
        available_agents = agents[:]

        for subtask in subtasks_sorted:
            best_match = None
            for agent in available_agents:
                if subtask.skill in agent.skills:
                    best_match = agent
                    break

            if best_match:
                assignments[subtask.id] = best_match.id
                available_agents.remove(best_match)
            else:
                assignments[subtask.id] = "no agent found"
        return assignments
