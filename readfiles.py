#adding path and storing it in a variable
text_file = open("Text.txt", "r")  # Text.txt is the file name i want to open,r means read.


# Check if the file is readable
print(text_file.readable())

# Read and print the entire content of the file
print(text_file.read())

# Reset the file cursor to the beginning of the file
text_file.seek(0)

# Read and print the first line of the file
print(text_file.readline())

# Read and print the second line of the file
print(text_file.readline())


# Close the file
text_file.close()
