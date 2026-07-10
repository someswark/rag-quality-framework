from golden_dataset_generators.mock_dataset_generator import (
    MockDatasetGenerator
)

from golden_dataset_generators.gemini_dataset_generator import (
    GeminiDatasetGenerator
)


class GeneratorFactory:

    @staticmethod
    def create(mode, context):

        if mode == "mock":

            return MockDatasetGenerator()

        elif mode == "gemini":

            return GeminiDatasetGenerator(context)
            
            
        elif mode == "openai":

            return OpenaiDatasetGenerator(context)

        raise ValueError(
            f"Unsupported generator mode : {mode}"
        )