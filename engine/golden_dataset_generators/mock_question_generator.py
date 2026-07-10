from question_generators.question_generator import QuestionGenerator


class MockQuestionGenerator(QuestionGenerator):

    def generate(self, chunk):

        return {

            "category": "HR",

            "question":
                "What is the company's leave policy?",

            "expected_answer":
                "Employees are entitled to annual leave according to company policy."

        }