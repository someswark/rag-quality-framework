from abc import ABC, abstractmethod


class BaseEvaluator(ABC):

    @abstractmethod
    def evaluate(self, dataset):
        """
        Returns a list of EvaluationResult objects.
        """
        pass