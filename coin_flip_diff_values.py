### This program calculates no. of times different values come when a coin is flipped 10,000 times
import random
def coin_flip():
    if(random.randint(0,1))==0:
        return "heads"
    else:
        return "tails"
count=0
prev=coin_flip()
for flip in range(10_000-1):
    flip=coin_flip()
    if flip=="heads" and prev=="tails":
        count=count+1
        prev="heads"
    elif flip=="tails" and prev=="heads":
        count=count+1
        prev="tails"
    else:
        continue
print(f"Out of 10,000 times {count} times coin flip resulted into different values!!")