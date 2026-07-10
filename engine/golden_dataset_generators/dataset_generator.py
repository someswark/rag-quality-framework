from abc import ABC, abstractmethod


class DatasetGenerator(ABC):

    @abstractmethod
    def generate(self, chunk):

        pass