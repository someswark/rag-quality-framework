import json
from pathlib import Path


class MockAnswerRepository:

    def __init__(self):

        file_path = (
            Path(__file__).parent.parent
            / "data"
            / "mock_answers.json"
        )

        with open(file_path, "r", encoding="utf-8") as file:
            self.answers = json.load(file)

    def get_answer(self, question):

        return self.answers.get(question)