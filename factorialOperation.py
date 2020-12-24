"""
Traning : Factorial operation
"""

num = int(input("Number : "))

factorial = 1

if num<0:
    print("Negative numbers cannot be calculated with a factorial")
    
elif num==0:
    print("Operation result : 1")

else:
    for i in range(1,num+1):
        factorial = factorial * i
    print("Operation result : ",factorial)

