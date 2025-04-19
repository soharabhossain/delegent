# Agent Registry
from delegent.core.agents.agent import Agent
from delegent.core.agents.agent_registry import AgentRegistry

REGISTRY_FILE = "./workspace/agents/agent_registry.json"

# Load existing registry or create a new one
registry = AgentRegistry.load_from_file(REGISTRY_FILE)

# Register new agents if not already present
if not registry.get_agent_by_id("A1"):
    registry.register(Agent(id="A1", role="writer", skills=["writing", "editing"]))
    registry.register(Agent(id="A2", role="researcher", skills=["research"]))
    registry.register(Agent(id="A3", role="designer", skills=["design"]))
    registry.register(Agent(id="A4", role="editor", skills=["editing", "video editing"]))
    registry.save_to_file(REGISTRY_FILE)

agents = registry.get_all()

for agent in agents:
    print(agent)
