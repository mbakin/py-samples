""" 
training to change the values ​​of numbers
"""

x = int(input("Number1 = "))
y = int(input("Number2 = "))

if x == y:
    print("Please, enter different numbers !")

    
temp = x
x = y
y=temp

print("New x value = " + str(x))
print("New y value = " + str(y))



