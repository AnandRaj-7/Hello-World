# def fibonacci(n):
#     ''' F(0)=0
#         F(1)=1
#         F(n)=F(n-1)+F(n-2)
#         0,1,1,2,3,5,8'''
#     if(n==0):
#         return 0
#     elif (n==1):
#         return 1
#     else:
#         return fibonacci(n-1)+fibonacci(n-2)
x = int(input("Enter a number : "))
# print("The sum of the fibonacci series is : ",fibonacci(x))
# fibonacci using simple loop
if x==0 or x==1:
    fib=x
    print("The sum of the fibonacci series is : ",fib)
else:
    a=0
    b=1
    fib=0
    for count in range(1,x):
        fib = a + b
        a = b
        b = fib
    print("The sum of the fibonacci series is : ",fib)
# set1 = {}
# print(type(set1))
# set1 = set()
# print(type(set1))