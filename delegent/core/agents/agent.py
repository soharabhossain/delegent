from delegent.utils.logger import log_step

class Agent:
    def __init__(self, id, role, skills):
        self.id = id
        self.role = role
        self.skills = skills

    def can_handle(self, subtask):
        return subtask['skill'] in self.skills and subtask['role'] == self.role

    def to_dict(self):
        return {'id': self.id, 'role': self.role, 'skills': self.skills}
    
    def __repr__(self):
        return f"Agent(id={self.id}, role={self.role})"
    
    @staticmethod
    @log_step("AgentCreationFromDict")
    def from_dict(data: dict):
        return Agent(
            id=data["id"],
            role=data["role"],
            skills=data.get("skills", [])
        )
