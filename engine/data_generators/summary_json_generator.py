import json
from pathlib import Path


class SummaryJsonGenerator:

    def __init__(self, context):

        self.context = context

    def generate(self, summary):

        output_path = (
            Path(__file__).parent.parent.parent
            / "website"
            / "assets"
            / "data"
            / "summary.json"
        )

        data = {

            "framework": {
                "name": "Enterprise AI Quality Framework",
                "version": "2.0"
            },

            "evaluation": {

                "total_questions": summary.total_questions,

                "pass_count": summary.pass_count,

                "review_count": summary.review_count,

                "fail_count": summary.fail_count,

                "overall_score": summary.overall_score,

                "quality_rating": summary.quality_rating,

                "average_confidence": summary.average_confidence,

                "average_latency": summary.average_latency

            }

        }

        with open(output_path, "w", encoding="utf-8") as file:

            json.dump(data, file, indent=4)

        print()
        print("✓ summary.json generated successfully")
        print(output_path)