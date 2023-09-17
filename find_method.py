n=2.0
x=input("Enter some text : ")
if(x.find(str(n))==-1):
    print("The input text doesn't contain 2.0!!")
else:
    print(f"{n} occurs at index {x.find(str(n))}th position")
y=input("Enter a string : ")
if y.find("x") != -1:
    print(f"x occurs at {y.find('x')}th position!!")
else:
    print("x is not present in your string!!")