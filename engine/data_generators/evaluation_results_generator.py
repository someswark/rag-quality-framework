import json
from pathlib import Path


class EvaluationResultsGenerator:

    def __init__(self, context):

        self.context = context

    def generate(self, results):

        output_path = (
            Path(__file__).parent.parent.parent
            / "website"
            / "assets"
            / "data"
            / "evaluation_results.json"
        )

        data = []

        for result in results:

            data.append({

                "question_id": result.question_id,
                "category": result.category,
                "question": result.question,
                "expected_answer": result.expected_answer,
                "generated_answer": result.generated_answer,
                "confidence": result.confidence,
                "latency_ms": result.latency_ms,
                "status": result.status

            })

        with open(output_path, "w", encoding="utf-8") as file:

            json.dump(data, file, indent=4)

        print()
        print("✓ evaluation_results.json generated successfully")