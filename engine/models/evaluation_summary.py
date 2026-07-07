from dataclasses import dataclass


@dataclass
class EvaluationSummary:

    total_questions: int

    pass_count: int

    review_count: int

    fail_count: int

    overall_score: float

    average_confidence: float

    average_latency: float
    
    quality_rating: str