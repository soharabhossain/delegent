# multi_agent_system/execution/execution_layer.py

from typing import Dict, List
from delegent.core.tasks.subtask import Subtask
from delegent.core.agents.agent import Agent
from delegent.utils.logger import log_step


class ExecutionResult:
    def __init__(self, subtask_id: str, agent_id: str, status: str, output: str):
        self.subtask_id = subtask_id
        self.agent_id = agent_id
        self.status = status  # e.g., 'completed', 'failed'
        self.output = output

    def to_dict(self):
        return {
            "subtask_id": self.subtask_id,
            "agent_id": self.agent_id,
            "status": self.status,
            "output": self.output
        }

class AgentExecutionLayer:
    def __init__(self):
        self.execution_logs: List[ExecutionResult] = []

    @log_step("AgentExecution")
    def execute(self, 
                subtasks: List[Subtask], 
                agents: List[Agent], 
                assignments: Dict[str, str]) -> List[ExecutionResult]:

        agent_dict = {agent.id: agent for agent in agents}

        for subtask in subtasks:
            agent_id = assignments.get(subtask.id)
            agent = agent_dict.get(agent_id)

            if not agent:
                result = ExecutionResult(subtask.id, "N/A", "failed", "No agent found")
            elif subtask.skill not in agent.skills:
                result = ExecutionResult(subtask.id, agent.id, "failed", f"Agent lacks skill: {subtask.skill}")
            else:
                output_msg = f"{agent.role.title()} ({agent.id}) executed subtask '{subtask.desc}' using skill '{subtask.skill}'"
                result = ExecutionResult(subtask.id, agent.id, "completed", output_msg)

            self.execution_logs.append(result)

        return self.execution_logs

    def get_logs(self) -> List[Dict]:
        return [res.to_dict() for res in self.execution_logs]
