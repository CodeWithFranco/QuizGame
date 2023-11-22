"""
Author: Franco Nepomuceno
Description: Using OOP with constructors, methods, and attributes from a loop
Date: 08 November 2023
Rev: A
"""
from typing import List

from question_model import Question
from data import question_data
from quiz_brain import QuizBrain

question_bank = []
for item in question_data:
    question_text = item["question"]  # The word 'text' is in the dictionary / list
    question_answer = item["correct_answer"]  # The word 'answer' is in the dictionary / list
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
"""
At this point each every item in 'question_bank' is in a memory slot. An object needs to be created in order to get
the actual question. 
# To get the dictionary key items:
  question_data[0]["text"] # where 0 is the number of list just like the for loop above
"""
quiz = QuizBrain(question_bank)  # object for QuizBrain class

while quiz.still_has_question:
    quiz.next_question()

print("You've completed the quiz")
print(f"Your final score was: {quiz.score}/{len(question_bank)} ")
# quiz.question_number: To get the current number of questions (alternate solution)
