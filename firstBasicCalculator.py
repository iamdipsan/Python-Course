num1 = input("Enter first number : ")
num2 = input("Enter second number: ")
#the number you take form the user is a string by default so before adding we need to convert
#the numbers you took as input  to a integer to add it. orelse it will just concatenate the
#two result give answer  : 2030
result = int(num1)  +int(num2) #this will only work for integer , if you want decimal value too,  use float.   
print(result)
