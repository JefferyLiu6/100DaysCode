from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for i in question_data:
    question_test = i["text"]
    question_answer = i["answer"]
    new_question = Question(question_test,question_answer)
    question_bank.append(new_question)

quiz = QuizBrain(question_bank)

while quiz.still_has_question():
    quiz.next_question()

print("You have completed this quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)}")