from data import question_data
from question_model import Question
from quiz_brain import QuizBrain
import os


question_bank = []
for question in question_data:
    question_bank.append(Question(question["question"],question["correct_answer"]))


quiz = QuizBrain(question_bank)

while quiz.still_has_questions():
    quiz.next_question()

print(f"This is the end of the quiz. \n\
your final score is: {quiz.score} \n\
you have answered {quiz.question_number} questions")
