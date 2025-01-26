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
quiz.next_question()