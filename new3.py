import sys
name=input("Hello Sir! \nEnter Your Name : ")
print("Hello Mr. "+name+"\nEnter your address : ")
address = sys.stdin.readlines()
addr=""
i=0
while i!=len(address):
    addr=addr+address[i]
    i=i+1
print("Hello Mr. "+name)
print("Your Address is : ")
print(addr)