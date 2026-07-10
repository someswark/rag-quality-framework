from answer_providers.mock_answer_provider import MockAnswerProvider
from answer_providers.gemini_answer_provider import GeminiAnswerProvider

class ProviderFactory:

    @staticmethod
    def create(provider, context):

        if provider == "mock":

            return MockAnswerProvider()

        elif provider == "gemini":

            return GeminiAnswerProvider(context)
            
            
        raise ValueError(
            f"Unsupported Answer Provider: {provider}"
        )