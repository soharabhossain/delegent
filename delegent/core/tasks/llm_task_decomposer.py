# multi_agent_system/llm/llm_task_decomposer.py


import json
from delegent.llm.llm_provider import get_llm_response
from delegent.core.tasks.subtask import Subtask
from delegent.core.tasks.task import Task
from delegent.utils.logger import log_step

class LLMTaskDecomposer:
    @log_step("LLMTaskDecomposer")
    def decompose(self, task: Task, agent_profiles: list) -> list:
        prompt = f"""
        Decompose the following task into subtasks relevant to the given agent profiles.
        Return only the json output and no additional text.

        Task: {task.description}
        Agent Profiles: {json.dumps(agent_profiles)}
        """
        """
        # Output format (as JSON list): 
        # [
        #     {{
        #         "id": "T200_1",
        #         "desc": "Subtask description",
        #         "skill": "required skill",
        #         "role": "expected role",
        #         "priority": 1
        #     }},
        #     ...
        # ]
        """
        response = get_llm_response(prompt)
        # print(response)
        # print("\n+++++++++++++++++++\n\n")
        try:
            # raw_subtasks = json.loads(response)
            # print(raw_subtasks)
            # print(response)
            raw_subtasks=response
            return [subtask for subtask in raw_subtasks]
        except json.JSONDecodeError as e:
            print("LLM response could not be parsed: ", e)
            return []


