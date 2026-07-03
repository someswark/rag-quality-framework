class Question:

    def __init__(
        self,
        question_id,
        category,
        question,
        expected_answer
    ):

        self.question_id = question_id
        self.category = category
        self.question = question
        self.expected_answer = expected_answer

    def __str__(self):

        return f"[{self.question_id}] {self.question}"