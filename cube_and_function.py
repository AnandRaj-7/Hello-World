import math
def cube(number):
    return number**3
def greet(name):
    print("Hello "+name+"!")
x=input("Enter a number: ")
print(f"The cube of the number {x} is "+str(cube(int(x))))
y=input("Hello Sir! what is your name ? ")
greet(y)