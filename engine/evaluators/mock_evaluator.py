from evaluators.base_evaluator import BaseEvaluator
from repositories.mock_answer_repository import MockAnswerRepository
from models.evaluation_result import EvaluationResult


class MockEvaluator(BaseEvaluator):

    def __init__(self, context):

        self.context = context
        self.repository = MockAnswerRepository()

    def evaluate(self, dataset):

        print()
        print("Running Mock Evaluation")
        print("-" * 60)

        results = []

        for question in dataset:

            mock = self.repository.get_answer(question.question)

            if mock is None:

                print(f"❌ No mock answer found for: {question.question}")
                continue

            result = EvaluationResult(

                question_id=question.question_id,
                category=question.category,
                question=question.question,
                expected_answer=question.expected_answer,
                generated_answer=mock["generated_answer"],
                confidence=mock["confidence"],
                latency_ms=mock["latency_ms"],
                status=mock["status"]

            )

            results.append(result)

            print(result)

        print()
        print("=" * 60)
        print(f"Evaluation Results Generated : {len(results)}")
        print("=" * 60)

        return results