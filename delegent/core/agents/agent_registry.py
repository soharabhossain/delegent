# multi_agent_system/agents/agent_registry.py

import json
from typing import List, Dict, Optional
from delegent.core.agents.agent import Agent

class AgentRegistry:
    def __init__(self):
        self.agents: Dict[str, Agent] = {}

    def register(self, agent: Agent):
        self.agents[agent.id] = agent

    def get_agent_by_id(self, agent_id: str) -> Optional[Agent]:
        return self.agents.get(agent_id)

    def find_agents_by_skill(self, skill: str) -> List[Agent]:
        return [a for a in self.agents.values() if skill in a.skills]

    def find_agents_by_role(self, role: str) -> List[Agent]:
        return [a for a in self.agents.values() if a.role == role]

    def find_agents_by_skill_and_role(self, skill: str, role: str) -> List[Agent]:
        return [a for a in self.agents.values() if skill in a.skills and a.role == role]

    def get_all(self) -> List[Agent]:
        return list(self.agents.values())

    def to_dict(self) -> List[Dict]:
        return [agent.to_dict() for agent in self.agents.values()]

    def save_to_file(self, path: str):
        with open(path, "w") as f:
            json.dump(self.to_dict(), f, indent=4)

    @staticmethod
    def load_from_file(path: str) -> 'AgentRegistry':
        registry = AgentRegistry()
        try:
            with open(path, "r") as f:
                data = json.load(f)
                for agent_data in data:
                    agent = Agent.from_dict(agent_data)
                    registry.register(agent)
        except FileNotFoundError:
            print(f"Warning: No registry found at {path}. A new one will be created.")
        return registry
