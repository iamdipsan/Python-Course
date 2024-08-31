numbers = [4, 6, 88, 3, 0, 34]
friends = ["Roi", "alex", "jimmy", "joseph", "kevin", "tony", "jimmy"]

print(numbers)
print(friends)

friends.extend(numbers)  # Adds all elements in 'numbers' to the 'friends' list
friends.append("hulk")   # Adds 'hulk' to the end of the 'friends' list
friends.insert(1, "mikey")  # Inserts 'mikey' at index 1
friends.remove("Roi")    # Removes the first occurrence of 'Roi' from the 'friends' list

print(friends.index("mikey"))  # Prints the index of 'mikey' in the 'friends' list
print(friends.pop())  # Removes and prints the last item in the 'friends' list
print(friends)  # Prints the current state of the 'friends' list
friends.clear()  # Clears all elements from the 'friends' list

print(friends)  # Prints the empty 'friends' list after clearing

numbers.sort()  # Sorts the 'numbers' list in place
print(numbers)  # Prints the sorted 'numbers' list
