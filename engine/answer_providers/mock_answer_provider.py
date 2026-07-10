import json
from pathlib import Path

from answer_providers.answer_provider import AnswerProvider


class MockAnswerProvider(AnswerProvider):

    def __init__(self):

        project_root = Path(__file__).resolve().parents[2]

        self.mock_answers_file = (
            project_root
            / "data"
            / "mock"
            / "mock_answers.json"
        )

        with open(
            self.mock_answers_file,
            encoding="utf-8"
        ) as file:

            self.answers = json.load(file)

        print(f"Mock Answers Loaded : {self.mock_answers_file}")
        print(f"Total Mock Answers : {len(self.answers)}")

    def generate_answer(self, question):

        return self.answers.get(question)