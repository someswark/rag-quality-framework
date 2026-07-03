from evaluators.mock_evaluator import MockEvaluator


class EvaluatorFactory:

    EVALUATORS = {
        "mock": MockEvaluator,
        # "live": LiveEvaluator,
        # "agent": AgentEvaluator
    }

    @staticmethod
    def create(context):

        config_loader = context.get_config_loader()

        execution = config_loader.get_execution()

        mode = execution.get("mode", "mock").lower()

        evaluator_class = EvaluatorFactory.EVALUATORS.get(mode)

        if evaluator_class is None:
            raise ValueError(f"Unsupported execution mode: {mode}")

        print(f"Evaluation Mode : {mode}")

        return evaluator_class(context)