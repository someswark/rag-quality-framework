import csv
from pathlib import Path

from models.question import Question


class DatasetLoader:

    def __init__(self, context):

        self.context = context

    def load(self):

        dataset = []

        dataset_path = (
            Path(__file__).parent
            / "golden_dataset.csv"
        )

        with open(
            dataset_path,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                dataset.append(

                    Question(

                        question_id=row["id"],

                        category=row["category"],

                        question=row["question"],

                        expected_answer=row["expected_answer"]

                    )

                )

        return dataset