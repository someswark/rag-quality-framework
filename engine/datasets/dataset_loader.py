import csv
from pathlib import Path

from models.question import Question


class DatasetLoader:

    def __init__(self, context):

        self.context = context

    def load(self):

        dataset = []

        project_root = Path(__file__).resolve().parents[2]

        dataset_path = (
            project_root
            / "data"
            / "datasets"
            / "golden_dataset.csv"
        )

        print(f"Loading Dataset : {dataset_path}")

        with open(
            dataset_path,
            newline="",
            encoding="utf-8"
        ) as file:

            reader = csv.DictReader(file)

            for row in reader:

                dataset.append(

                    Question(

                        question_id=row["question_id"],

                        category=row["category"],

                        question=row["question"],

                        expected_answer=row["expected_answer"]

                    )

                )

        return dataset
        