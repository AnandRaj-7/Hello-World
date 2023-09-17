### [1,2,3,4]= [24,12,8,6]
list1=[1,2,3,4]
list2=[]
### count_zeros return -1 if in case no zeros are there, index position in case 1 zero is there and -2 in case 2 or more zeros are there
def count_zeros(check):
    count=0
    for i in range(len(check)):
        if(check[i]==0):
            pos=i
            count=count+1
            if count==2 :
                return -2
    if count==1 :
        return pos
    return -1
x=count_zeros(list1)
product=1
if x==-2 :
    for i in range(len(list1)):
        list2.insert(i,0)
elif x>0:
    for i in range(len(list1)):
        if i==x:
            continue
        list2.insert(i,0)
        product=product*list1[i]
    list2.insert(x,product)
else:
    for i in range(len(list1)):
        y=1
        for j in range(len(list1)):
            if i==j:
                continue
            else:
                y=y*list1[j]
        list2.insert(i,y)
print(list2)