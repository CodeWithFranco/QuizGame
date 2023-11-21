# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end

class QuizBrain:

    def __init__(self, q_list):  # initial value - as observed at main.py
        self.question_number = 0  # objects with values doesnt need to have an input. It has a default value
        self.question_list = q_list
        self.score = 0

    # TODO: Retrieve the item at the current question_number from the question_list.
    # TODO: Use the input() function to show the user the Question text and ask the user's answer

    def next_question(self):  # This is a method
        current_question = self.question_list[self.question_number]
        # current_question.text = object.attribute
        self.question_number += 1
        user_answer = input(f"Q{self.question_number}: {current_question.text} (True/False)\t")
        self.check_answer(user_answer, current_question.answer)

    def still_has_question(self):
        return self.question_number < len(self.question_list)

    def check_answer(self, user_answer, correct_answer):
        if user_answer.lower() == correct_answer.lower():
            print("You got it right!")
            self.score += 1


        else:
            print("That's wrong.")
        print(f"The correct answer was: {correct_answer}")
        print(f"Your current score is: {self.score}/{self.question_number}\n")


"""
# You can simplify this by using one line and an equation equallng to 'true or false'
if self.question_number < len(self.question_list):
    return True
 else:
    return False
"""
