x = 0
list1 =[]
try:
    while True:
            x = input("Please enter a number and enter 'q' to quit entering: ")
            if x == 'q':
                break
            list1.append(int(x))
    print(f"your list is {list1}")
    target = int(input("Enter a sum target: "))
    list2 = []
    for i in range(0,len(list1)):
        for j in range(i+1,len(list1)):
            if(list1[i]+list1[j] == target):
                list2.append([i,j])
    print("The list containing index pairs matching the sum target condition are: ",list2)
except:
    print("some error occured. Please rerun the program!!!")