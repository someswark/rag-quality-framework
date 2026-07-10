import time

from answer_providers.answer_provider import AnswerProvider
from llm.gemini_client import GeminiClient


class GeminiAnswerProvider(AnswerProvider):

    def __init__(self, context):

        self.context = context

        self.client = GeminiClient(context)

    def generate_answer(self, question):

        document = self.context.get_document_text()

        start = time.time()

        prompt = f"""
You are an enterprise AI assistant.

Answer ONLY from the document below.

If the answer is not present,
reply exactly:

Information not available.

----------------------------------

DOCUMENT

{document}

----------------------------------

QUESTION

{question}

----------------------------------

Return ONLY the answer.
"""

        answer = self.client.generate(prompt)

        latency = int((time.time() - start) * 1000)

        return {

            "generated_answer": answer.strip(),

            "latency_ms": latency

        }