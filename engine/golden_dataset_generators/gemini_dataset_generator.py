import json

from golden_dataset_generators.dataset_generator import DatasetGenerator
from llm.gemini_client import GeminiClient


class GeminiDatasetGenerator(DatasetGenerator):

    def __init__(self, context):

        self.client = GeminiClient(context)

    def generate(self, chunk):

        prompt = f"""
You are an AI Quality Engineer.

Read the document below and generate ONLY ONE evaluation record.

Return ONLY valid JSON.

Do not return markdown.
Do not return explanation.
Do not return code block.

JSON format:

{{
  "category":"",
  "question":"",
  "expected_answer":""
}}

Document:

{chunk}
"""

        response = self.client.generate(prompt)

        print("\nGemini Response:\n")
        print(response)

        response = response.replace("```json", "")
        response = response.replace("```", "")
        response = response.strip()

        return json.loads(response)