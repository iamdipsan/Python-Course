# Define a class to represent a quiz question
class Question:
    # Initialize the Question object with a prompt and the correct answer
    def __init__(self, prompt, answer):
        self.prompt = prompt  # The text of the question
        self.answer = answer  # The correct answer to the question
