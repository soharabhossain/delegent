import json

def load_agents(file_path):
    with open(file_path) as f:
        return json.load(f)

def load_tasks(file_path):
    with open(file_path) as f:
        return json.load(f)
