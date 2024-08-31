def exponentialFunction(base,power):
    result = 1
    for index in range(power):
        result = result * base
    return result

print(exponentialFunction(3,2))
print(exponentialFunction(4,2))
print(exponentialFunction(5,2))

#or you can power just by
print(2**3) #number *** power