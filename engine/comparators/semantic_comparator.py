from comparators.answer_comparator import AnswerComparator


class SemanticComparator(AnswerComparator):

    def compare(self, expected_answer, generated_answer):

        expected = expected_answer.lower().strip()
        generated = generated_answer.lower().strip()

        if expected == generated:

            confidence = 100
            status = "PASS"

        elif expected in generated or generated in expected:

            confidence = 90
            status = "PASS"

        else:

            confidence = 60
            status = "REVIEW"

        return {

            "confidence": confidence,

            "status": status

        }