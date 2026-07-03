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
        return self.config["framework"]

    def get_application(self):
        return self.config["application"]

    def get_llm(self):
        return self.config["llm"]

    def get_output(self):
        return self.config["output"]

    def get_evaluation(self):
        return self.config["evaluation"]