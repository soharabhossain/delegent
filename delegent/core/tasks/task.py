
# multi_agent_system/tasks/task.py

from delegent.utils.logger import log_step

class Task:
    def __init__(self, id: str, desc: str):
        self.id = id
        self.description = desc

    @log_step("TaskDecompose")
    def decompose(self):
        # Placeholder logic — customize per task ID or type
        if self.id == 'T200':
            return [
                {'id': f'{self.id}_1', 'desc': 'Research market trends', 'skill': 'research', 'role': 'researcher'},
                {'id': f'{self.id}_2', 'desc': 'Draft launch announcement', 'skill': 'writing', 'role': 'writer'},
                {'id': f'{self.id}_3', 'desc': 'Design infographics', 'skill': 'design', 'role': 'designer'},
                {'id': f'{self.id}_4', 'desc': 'Proofread final content', 'skill': 'editing', 'role': 'editor'},
                {'id': f'{self.id}_5', 'desc': 'Create a teaser video', 'skill': 'video editing', 'role': 'editor'}
            ]
        else:
            return []

