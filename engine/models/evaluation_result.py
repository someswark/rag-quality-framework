from dataclasses import dataclass


@dataclass
class EvaluationResult:

    question_id: str
    category: str

    question: str

    expected_answer: str
    generated_answer: str

    confidence: int

    latency_ms: int

    status: str

    def __str__(self):

        return (
            f"\nQuestion   : {self.question}"
            f"\nStatus     : {self.status}"
            f"\nConfidence : {self.confidence}%"
            f"\nLatency    : {self.latency_ms} ms"
        )