i= 1 

while i<=5:
    print(i)
    i=i+1 # or i++ or i += 1

print("Loop complete")


print("new example")

n = 5            # Set n to 5, which is the upper limit of the range (1 to 5)
sum = 0          # Initialize sum to 0, this will store the total sum of numbers
j = 1            # Initialize j to 1, this is the starting point of the loop

while j <= n:    # Start a while loop that will run as long as j is less than or equal to n (5)
    sum += j     # Add the current value of j to sum. Initially, sum = 0 + 1 = 1.
    j += 1       # Increment j by 1. Now, j becomes 2.

    # The loop will now check the condition again: j (2) <= n (5).
    # The steps repeat:
    # sum = sum + j -> sum = 1 + 2 = 3
    # j is incremented -> j becomes 3.

    # The loop continues:
    # sum = sum + j -> sum = 3 + 3 = 6
    # j is incremented -> j becomes 4.

    # The loop continues:
    # sum = sum + j -> sum = 6 + 4 = 10
    # j is incremented -> j becomes 5.

    # The loop continues:
    # sum = sum + j -> sum = 10 + 5 = 15
    # j is incremented -> j becomes 6.

    # Now, j (6) is greater than n (5), so the loop condition fails and the loop stops.

print("Sum of numbers from 1 to", n, "is:", sum)  # Print the final result.

# The final value of sum is 15, which is the sum of numbers from 1 to 5.
