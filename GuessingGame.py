guess_word = "cow"
guess = ""

while guess != guess_word:
    guess = input("Enter your guess animal: ")
    if guess != guess_word:
        print("Incorrect guess, please try again.")

print("Correct!")
print("You successfully guessed the animal:", guess_word)
