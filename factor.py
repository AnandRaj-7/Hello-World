x=input("Enter a positive integer: ")
if(int(x)>0):
    print("1 is the factor of "+x)
    fact=2
    int(x)/2
    while fact<=int(x)/2:
        if(int(x)%fact==0):
            print(f"{fact} is the factor of "+x)
        fact=fact+1
else:
    print("wrong input!!")