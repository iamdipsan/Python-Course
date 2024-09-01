# Import the Question class from the questions module
from questions import Question

# Define a list of question prompts with multiple-choice options
question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]

# Create a list of Question objects with corresponding answers
questions = [
    Question(question_prompts[0], "a"),  # First question, correct answer is 'a'
    Question(question_prompts[1], "c"),  # Second question, correct answer is 'c'
    Question(question_prompts[2], "b"),  # Third question, correct answer is 'b'
]

# Define a function to run the quiz
def run(questions):
    score = 0  # Initialize the score counter

    # Iterate over each question in the questions list
    for question in questions:
        # Prompt the user with the question and get their answer
        answer = input(question.prompt)
        
        # Check if the user's answer is correct
        if answer == question.answer:
            score += 1  # Increment the score for a correct answer

    # Print the final score and a congratulatory message
    print("Your score is " + str(score) + "/" + str(len(questions)) + ". Congrats!")

# Execute the run function with the list of questions
run(questions)
