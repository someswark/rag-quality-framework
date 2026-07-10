import os
import google.generativeai as genai


class GeminiClient:

    def __init__(self, context):

        config = context.get_config_loader().get_llm()

        api_key = (
            os.getenv("GOOGLE_API_KEY")
            or config.get("api_key")
        )

        if not api_key:
            raise ValueError(
                "Gemini API Key not configured."
            )

        genai.configure(api_key=api_key)

        self.model = genai.GenerativeModel(
            config.get("model")
        )

    def generate(self, prompt):

        response = self.model.generate_content(prompt)

        return response.text