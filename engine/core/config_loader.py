import json
from pathlib import Path


class ConfigLoader:

    def __init__(self):

        config_path = (
            Path(__file__).parent.parent
            / "config"
            / "framework-config.json"
        )

        with open(config_path, "r", encoding="utf-8") as file:
            self.config = json.load(file)

    def get(self):
        return self.config

    def get_framework(self):
        return self.config.get("framework", {})

    def get_execution(self):
        return self.config.get("execution", {})

    def get_application(self):
        return self.config.get("application", {})

    def get_knowledge_source(self):
        return self.config.get("knowledge_source", {})

    def get_llm(self):
        return self.config.get("llm", {})

    def get_evaluation(self):
        return self.config.get("evaluation", {})

    def get_output(self):
        return self.config.get("output", {})
        
    def get_answer_provider(self):

        return self.config.get(
        "answer_provider",
        {}
        )