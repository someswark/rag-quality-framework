from abc import ABC, abstractmethod


class QuestionGenerator(ABC):

    @abstractmethod
    def generate(self, chunk):

        pass