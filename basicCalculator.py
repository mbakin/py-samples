"""
Traning : Basic Calculator 
"""

def plus(num1,num2):
    return num1 + num2

def minus(num1,num2):
    return num1 - num2

def multiply_by(num1,num2):
    return num1 * num2

def divide_by(num1,num2):
    return num1 / num2

print("Select operation:")
print("1 : Addition")
print("2 : Substract")
print("3 : Multiply")
print("4 : Divide")

select = input("Select Operation : ")

num1 = int(input("First number = "))
num2 = int(input("Second number = "))

if select == '1':
    print("Addition : " +str(plus(num1,num2)))
elif select == '2':
    print("Substract : " +str(minus(num1,num2)))   
elif select == '3':
    print("Multiply : " +str(multiply_by(num1,num2))) 
elif select == '4':
    print("Divide : " +str(divide_by(num1,num2)))
else:
    print("Invalid option")


