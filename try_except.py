### This program asks the user for an integer if he inputs a text it keeps prompting until he enters an integer
### try and except is used for exception handling when user inputs string and not an integer
while True:
    try:
        x=int(input("Enter an integer: "))
        if int(x) or int(x)==0:
            print(f"You have entered {x} Good job!!\nProgram has terminated!!")
            break
    except ValueError:
        print("Try again!!")