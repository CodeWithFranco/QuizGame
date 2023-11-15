# TODO: asking the questions
# TODO: checking if the answer was correct
# TODO: checking if we're the end

class QuizBrain:

    def __init__(self, q_list):
        self.question_number = 0  # objects with values doesnt need to have an input
        self.question_list = q_list

# TODO: Retrieve the item at the current question_number from the question_list.
# TODO: Use the input() function to show the user the Question text and ask the user's answer

    def next_question(self):  # This is a method
        current_question = self.question_list[self.question_number]
        # current_question.text = object.attribute
        input(f"Q{self.question_number}: {current_question.text} (True/False)")