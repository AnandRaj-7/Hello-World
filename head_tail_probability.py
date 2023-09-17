### This program calculates the probability of heads and tails when a coin is tossed 10,000 times
import random
def coin_flip():
    if(random.randint(0,1))==0:
        return "heads"
    else:
        return "tails"
heads_tally=0
tails_tally=0
for flip in range(10_000):
    if coin_flip() == "heads":
        heads_tally=heads_tally+1
    else:
        tails_tally=tails_tally+1
print(f"The probability heads is {heads_tally}/{heads_tally+tails_tally} in 10,000 flips!!")
print(f"The probability tails is {tails_tally}/{heads_tally+tails_tally} in 10,000 flips!!")