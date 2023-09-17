### random throw of a dice and probability attached to it
import random
def roll():
    return random.randint(1,6)
avg1=0
avg2=0
avg3=0
avg4=0
avg5=0
avg6=0
for rolls in range(10_000):
    out=random.randint(1,6)
    if out==1 :
        avg1=avg1+1
    elif out==2 :
        avg2=avg2+1
    elif out==3 :
        avg3=avg3+1
    elif out==4 :
        avg4=avg4+1
    elif out==5 :
        avg5=avg5+1
    elif out==6:
        avg6=avg6+1
print(f"The average no. of times 1 occurs is {avg1} in 10,000 rolls of dice!!")
print(f"The average no. of times 2 occurs is {avg2} in 10,000 rolls of dice!!")
print(f"The average no. of times 3 occurs is {avg3} in 10,000 rolls of dice!!")
print(f"The average no. of times 4 occurs is {avg4} in 10,000 rolls of dice!!")
print(f"The average no. of times 5 occurs is {avg5} in 10,000 rolls of dice!!")
print(f"The average no. of times 6 occurs is {avg6} in 10,000 rolls of dice!!")