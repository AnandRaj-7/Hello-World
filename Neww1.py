class Dog:
    def __init__(self, name, age):
        self.name=name
        self.age=age
    def details(self):
        if type(self.name)==str and type(self.age)==int:
            print("Name is "+self.name+" and age is %d" %self.age)
        else:
            print("Opps! Wrong data")
            print("Enter data as String for name and number for age")
Tommy=Dog("Tommy",4)
Tommy.details()
Rocky=Dog("Rocky","Two")
Rocky.details()
a=input("Enter Name : ")
b=input("Enter age : ")
if b.isdigit() :
    b=int(b)
    Doggy=Dog(a,b)
    Doggy.details()
else:
    print("Wrong Data")