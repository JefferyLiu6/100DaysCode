class Question:
    def __init__(self, question, answer):
        self.question = question
        self.answer = answer


if __name__ == 'main':
    new_question = Question("asdgsd", "asfD")
    print(new_question.question)