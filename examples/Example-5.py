
# Agent Execution Layer
from delegent.core.execution.execution_layer import AgentExecutionLayer
from delegent.core.agents.agent import Agent
from delegent.core.tasks.subtask import Subtask

# 1. Create mock agents
agents = [
    Agent(id="a1", role="writer", skills=["writing", "editing"]),
    Agent(id="a2", role="designer", skills=["design", "illustration"]),
]

# 2. Create mock subtasks
subtasks = [
    Subtask(id="t1", desc="Write blog post", skill="writing", role="writer"),
    Subtask(id="t2", desc="Design banner", skill="design", role="designer"),
    Subtask(id="t3", desc="Proofread article", skill="editing", role="editor"),
    Subtask(id="t4", desc="Develop software", skill="coding, programming", role="software developer")  # Should fail
]

# 3. MOCK assignment dict: subtask_id -> agent_id
assignments = {
    "t1": "a1",  # Success
    "t2": "a2",  # Success
    "t3": "a1",  # Success
    "t4": "a1" #Fail (role mismatch)
}

# 4. Call execution layer
execution_layer = AgentExecutionLayer()
results = execution_layer.execute(subtasks=subtasks, agents=agents, assignments=assignments)

# 5. Print results
for result in results:
    print(f"SubTask ID: {result.subtask_id} -> Agent ID: {result.agent_id} -> Status: {result.status}")

