from metrics.base_metric import BaseMetric


class AccuracyMetric(BaseMetric):

    def calculate(self, expected_answer, generated_answer):

        expected = expected_answer.lower().strip()
        generated = generated_answer.lower().strip()

        if expected == generated:

            score = 100
            reason = "Generated answer exactly matches the expected answer."

        elif expected in generated or generated in expected:

            score = 90
            reason = "Generated answer partially matches the expected answer."

        else:

            score = 60
            reason = "Generated answer differs from the expected answer."

        return {

            "metric": "Accuracy",

            "score": score,

            "reason": reason

        }