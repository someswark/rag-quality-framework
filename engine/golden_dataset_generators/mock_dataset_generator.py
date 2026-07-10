from golden_dataset_generators.dataset_generator import DatasetGenerator


class MockDatasetGenerator(DatasetGenerator):

    def generate(self, chunk):

        text = chunk.lower()

        if "leave" in text:

            return {
                "category": "HR",
                "question": "What is the company's leave policy?",
                "expected_answer": "Employees are entitled to annual leave according to the company leave policy."
            }

        elif "password" in text:

            return {
                "category": "IT",
                "question": "How do I reset my password?",
                "expected_answer": "Passwords can be reset using the self-service password reset portal."
            }

        elif "employee handbook" in text:

            return {
                "category": "HR",
                "question": "Where can I find the employee handbook?",
                "expected_answer": "The employee handbook is available on the company intranet."
            }

        return {
            "category": "General",
            "question": "What information is available in this document?",
            "expected_answer": chunk[:150]
        }