### factor program without loop
x=input("Enter a positive integer: ")
fact=2
if int(x)>0:
    print("1 is the factor of "+x)
    if(int(x)%fact==0):
        print(f"{fact} is the factor of "+x)
        fact=fact+1
        if (fact>int(x)/2):
            exit
else:
    print("wrong input!!")