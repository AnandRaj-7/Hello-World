import math
x = input("Enter any value between 5 and 9 : ")
if(x.isdigit()):
    x=int(x)
    if (x<5 or x>9):
        raise ValueError("Value should be between 5 and 9!!!")
    else:
        print("You entered ",x)
else:
    if x=='quit':
        print("You ended the program!!!")
    else:
        raise ValueError("Value should be between 5 and 9!!!")