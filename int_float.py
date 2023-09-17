input1=input("Enter first number : ")
input2=input("Enter second number : ")
if input1.isdigit()  and input2.isdigit():
    print(float(int(input1)*int(input2)))
else:
    print("Oops wrong data, characters not allowed!!!")