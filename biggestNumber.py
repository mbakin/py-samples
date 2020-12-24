"""
Traning: Which number is the biggest
"""

number1 = float(input("First Number = " ))
number2 = float(input("Second Number = "))
number3 = float(input("Third Number = "))

a = [number1, number2, number3]

a.sort()

print("Sorted Values = " + str(a))

print("************************")

if number1>number2 and number1>number3:
    print("Number 1 biggest than values")
    
elif number2>number3 and number3>number1:
    print("Number 2 biggest in values")
    
else:
    print("Number 3 biggest than values")
    
