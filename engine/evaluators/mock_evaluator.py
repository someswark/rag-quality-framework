from evaluators.base_evaluator import BaseEvaluator
from answer_providers.provider_factory import ProviderFactory
from models.evaluation_result import EvaluationResult
from metrics.metric_engine import MetricEngine


class MockEvaluator(BaseEvaluator):

    def __init__(self, context):

        self.context = context

        config = (
            context
            .get_config_loader()
            .get_answer_provider()
        )

        self.provider = ProviderFactory.create(
            config.get("provider"),
            context
        )

        self.metric_engine = MetricEngine()

    def evaluate(self, dataset):

        print()
        print("Running Evaluation")
        print("-" * 60)

        results = []

        for question in dataset:

            answer = self.provider.generate_answer(
                question.question
            )

            if answer is None:

                print(
                    f"❌ No answer found for: {question.question}"
                )

                continue

            # -----------------------------------------
            # Run all quality metrics
            # -----------------------------------------

            metric_results = self.metric_engine.evaluate(

                question.expected_answer,

                answer["generated_answer"]

            )

            accuracy = metric_results["accuracy"]["score"]

            confidence = self.metric_engine.calculate_overall_score(
                metric_results
            )

            status = self.metric_engine.determine_status(
                confidence
            )

            # -----------------------------------------
            # Build Evaluation Result
            # -----------------------------------------

            result = EvaluationResult(

                question_id=question.question_id,

                category=question.category,

                question=question.question,

                expected_answer=question.expected_answer,

                generated_answer=answer["generated_answer"],

                accuracy=accuracy,

                confidence=confidence,

                latency_ms=answer["latency_ms"],

                status=status

            )

            results.append(result)

            print(result)

        print()
        print("=" * 60)
        print(
            f"Evaluation Results Generated : {len(results)}"
        )
        print("=" * 60)

        return results