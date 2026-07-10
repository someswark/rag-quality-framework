from abc import ABC, abstractmethod


class AnswerProvider(ABC):

    @abstractmethod
    def generate_answer(self, question):

        pass