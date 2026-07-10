import csv
from pathlib import Path
#from dataset_generators.generator_factory import GeneratorFactory
from golden_dataset_generators.generator_factory import GeneratorFactory


class GoldenDatasetGenerator:

    def __init__(self, context):

        self.context = context

        self.config_loader = context.get_config_loader()

    def generate(self, chunks):

        config = self.config_loader.get_knowledge_source()

        generator = GeneratorFactory.create(
            config.get("mode"),
            self.context
        )

        output = (
            Path(__file__).resolve().parents[2]
            / "data"
            / "datasets"
            / "golden_dataset.csv"
        )

        output.parent.mkdir(
            parents=True,
            exist_ok=True
        )

        with open(
            output,
            "w",
            newline="",
            encoding="utf-8"
        ) as csvfile:

            writer = csv.writer(csvfile)

            writer.writerow([
                "question_id",
                "category",
                "question",
                "expected_answer"
            ])

            config = self.config_loader.get_knowledge_source()

            max_questions = config.get("max_questions", len(chunks))

            for index, chunk in enumerate(chunks[:max_questions]):

                result = generator.generate(chunk)

                writer.writerow([

                    index + 1,

                    result["category"],

                    result["question"],

                    result["expected_answer"]

                ])

        print(f"Golden Dataset Generated : {output}")