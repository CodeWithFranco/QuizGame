
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
    question_text = item["text"]  # The word 'text' is in the dictionary / list
    question_answer = item["answer"]  # The word 'answer' is in the dictionary / list
    new_question = Question(question_text, question_answer)
    question_bank.append(new_question)
"""
At this point each every item in 'question_bank' is in a memory. An object needs to be created in order to get
the actual question. 
"""
quiz = QuizBrain(question_bank)  # object for QuizBrain class
quiz.next_question()
