from dataclasses import dataclass


@dataclass
class EvaluationResult:

    # ----------------------------------------
    # Question Information
    # ----------------------------------------

    question_id: str
    category: str

    question: str

    expected_answer: str
    generated_answer: str

    # ----------------------------------------
    # Individual AI Quality Metrics
    # ----------------------------------------

    accuracy: int = 0

    grounding: int = 0

    completeness: int = 0

    hallucination: int = 0

    safety: int = 0

    # ----------------------------------------
    # Overall Evaluation
    # ----------------------------------------

    confidence: int = 0

    latency_ms: int = 0

    status: str = "REVIEW"

    # ----------------------------------------
    # Metric Details (Future Use)
    # ----------------------------------------

    accuracy_reason: str = ""

    grounding_reason: str = ""

    completeness_reason: str = ""

    hallucination_reason: str = ""

    safety_reason: str = ""

    def __str__(self):

        return (
            f"\nQuestion        : {self.question}"
            f"\nCategory        : {self.category}"
            f"\n"
            f"\nAccuracy        : {self.accuracy}%"
            f"\nGrounding       : {self.grounding}%"
            f"\nCompleteness    : {self.completeness}%"
            f"\nHallucination   : {self.hallucination}%"
            f"\nSafety          : {self.safety}%"
            f"\n"
            f"\nOverall Score   : {self.confidence}%"
            f"\nStatus          : {self.status}"
            f"\nLatency         : {self.latency_ms} ms"
        )