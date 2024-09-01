def translator(phrase):
    translation = ""
    # Loop through each letter in the input phrase
    for letter in phrase:
        # Check if the letter is a vowel (both uppercase and lowercase)
        if letter.lower() in "aeiou":
            # If the vowel is uppercase, add 'G' to the translation
            if letter.isupper():
                translation += "G"
            # If the vowel is lowercase, add 'g' to the translation
            else:
                translation += "g"
        # If the letter is not a vowel, add it to the translation as is
        else:
            translation += letter
    # Return the final translated phrase
    return translation

# Take input from the user and print the translated phrase
print(translator(input("Enter a phrase: ")))
