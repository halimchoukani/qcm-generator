# validator.py

class QuestionValidator:
    def validate(self, questions):
        validated_questions = []
        for question in questions:
            if self.is_valid(question):
                validated_questions.append(question)
        return validated_questions

    def is_valid(self, question):
        if not question.get("question") or not question.get("choices") or not question.get("correct"):
            return False
        if len(question["choices"]) != 4:
            return False
        if question["correct"] not in question["choices"]:
            return False
        return True
