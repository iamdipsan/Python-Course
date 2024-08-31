# The word that the user needs to guess
guess_word = "cow"
# Initialize guess as an empty string
guess = ""
# Set the maximum number of allowed guesses
limit = 5
# Initialize the count of guesses made
guess_count = 0
# Flag to check if the guess limit has been exceeded
crossed_limit = False

# Loop until the user guesses correctly or exceeds the guess limit
#Runs as long as the user’s guess is not equal to guess_word and the guess limit has not been crossed.
while guess != guess_word and not crossed_limit:
    # Check if the number of guesses made is less than the limit
    if guess_count < limit:
        # Prompt the user to enter their guess
        guess = input("Enter your guess animal: ")
        # Check if the guess is not correct
        if guess != guess_word:
            print("Incorrect guess, please try again.")  # Inform the user to try again
            guess_count += 1  # Increment the count of guesses made
        else:
            # If the guess is correct, congratulate the user and exit the loop
            print("You successfully guessed the animal:", guess_word)
            break
    else:
        # If the number of guesses reaches the limit, set the flag and inform the user
        crossed_limit = True
        print("You've crossed the limit of guesses.")

# After exiting the loop, check if the guess limit was crossed
if crossed_limit:
    print("Guessing limited was croessed.")
