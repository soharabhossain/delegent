
import os
from dotenv import load_dotenv
load_dotenv()

from delegent.core.tasks.subtask import SubtaskList
from instructor import patch, from_groq


# Dynamic import based on LLM_PROVIDER
def get_llm_response(prompt: str) -> str:
    if os.environ["LLM_PROVIDER"] == "openai":
        import openai
        # Apply patch to OpenAI client
        client = patch(openai.OpenAI())

        # Call the LLM
        response = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant that decomposes tasks."},
                {"role": "user", "content": prompt}
            ],
            response_model=SubtaskList
        )
        structured_subtasks = response.subtasks
        return structured_subtasks

    elif os.environ["LLM_PROVIDER"] == "groq":
        import groq
        groq_client = groq.Groq()

        # Patch Groq client
        client = from_groq(groq_client)

        # Call Groq LLM
        response = client.chat.completions.create(
            model="meta-llama/llama-4-scout-17b-16e-instruct",
            messages=[
                {"role": "system", "content": "You decompose high-level tasks into subtasks."},
                {"role": "user", "content": prompt}
            ],
            response_model=SubtaskList
        )
        structured_subtasks = response.subtasks
        return structured_subtasks

    else:
        raise ValueError("Unsupported LLM provider")




