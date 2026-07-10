from abc import ABC, abstractmethod


class BaseMetric(ABC):

    @abstractmethod
    def calculate(self, expected_answer, generated_answer):

        pass