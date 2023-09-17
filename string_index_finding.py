### This program prompts user to input a string and an index postion to check for the character at that index position
try:
    str1=input("Enter a string: ")
    n=int(input("Enter an integer: "))
    print(f"The letter at {n}th position is "+str1[n-1])
except ValueError:
    print("Oops, you have not entered and integer!!")
except IndexError:
    print("The index postion you entered is invalid!!")