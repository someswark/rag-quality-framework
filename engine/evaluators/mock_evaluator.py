from evaluators.base_evaluator import BaseEvaluator


class MockEvaluator(BaseEvaluator):

    def __init__(self, context):

        self.context = context

    def evaluate(self, dataset):

        print()

        print("Running Mock Evaluation")

        print("-" * 50)

        for question in dataset:

            print(question)

        print()

        return []