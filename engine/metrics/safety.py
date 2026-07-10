from metrics.base_metric import BaseMetric


class SafetyMetric(BaseMetric):

    def calculate(self, expected_answer, generated_answer):

        return 100