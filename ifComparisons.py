def max_numbers(num1,num2,num3):
    if num1>=num2 and num1 >=num3: 
        return num1
    elif num2>=num1 and num2>=num3:
        return num2
    else:
        return num3

print(max_numbers(20,40,60))
print(max_numbers(30,14,20))
print(max_numbers(3,90,10))

print("For min_number")

def min_numbers(num1,num2,num3):
    if num1<=num2 and num1<=num3: 
        return num1
    elif num2<=num1 and num2<=num3:
        return num2
    else:
        return num3

print(min_numbers(20,40,60))
print(min_numbers(30,14,20))
print(min_numbers(3,90,10))


