# multi_agent_system/tasks/subtask.py

from typing import List, Dict, Optional
from delegent.core.tasks.task import Task
from pydantic import BaseModel


class Subtask(BaseModel):
    id: str
    desc: str
    skill: str
    role: str
    priority: Optional[int] = None
    
    def __repr__(self):
        return f"<Subtask {self.id}: {self.desc}>"

    @staticmethod
    def from_task(task: Task) -> List['Subtask']:
        # For now, use static mapping for demonstration; can be improved with NLP, etc.
        if task.id == "T200":
            return [
                Subtask(id='T200_1', desc='Research market trends', skill='research', role='researcher'),
                Subtask(id='T200_2', desc='Draft launch announcement', skill='writing', role='writer'),
                Subtask(id='T200_3', desc='Design infographics', skill='design', role='designer'),
                Subtask(id='T200_4', desc='Proofread final content', skill='editing', role='editor'),
                Subtask(id='T200_5', desc='Create a teaser video', skill='video editing', role='editor')
            ]
        else:
            return []  # Default: no subtasks generated

    @staticmethod
    def from_dict(data: Dict) -> 'Subtask':
        return Subtask(
            id=data['id'],
            desc=data['desc'],
            skill=data['skill'],
            role=data['role'],
            )


class SubtaskList(BaseModel):
    subtasks: List[Subtask]
