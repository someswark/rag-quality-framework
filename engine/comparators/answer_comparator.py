from abc import ABC, abstractmethod


class AnswerComparator(ABC):

    @abstractmethod
    def compare(self, expected_answer, generated_answer):

        pass