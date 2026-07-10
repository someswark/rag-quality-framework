from metrics.base_metric import BaseMetric


class CompletenessMetric(BaseMetric):

    def calculate(self, expected_answer, generated_answer):

        if len(generated_answer) >= len(expected_answer):

            return 100

        return 80