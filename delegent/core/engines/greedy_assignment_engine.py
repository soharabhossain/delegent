from .assignment_engine import AssignmentEngine

class GreedyAssignmentEngine(AssignmentEngine):
    """
    Greedy assignment strategy: Assigns the first available agent
    who can perform the subtask based on required skill.
    Does not consider role, just matches skills.
    """

    def assign(self, subtasks, agents):
        assignments = {}
        available_agents = agents.copy()

        for subtask in subtasks:
            assigned = False
            for agent in available_agents:
                if subtask['skill'] in agent['skills']:
                    assignments[subtask['id']] = agent['id']
                    available_agents.remove(agent)
                    assigned = True
                    break

            if not assigned:
                assignments[subtask['id']] = None  # No suitable agent found

        return assignments
