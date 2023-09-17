### Election simulation 
### Here in Region 1 Candidate A has 87% chance, in Region 2 Candidate A has 65% chance and in Region 3 Candidate A has 17% chance
### The logic here is if Region 1 comes Candidate A gets 87 votes and Candidtate B gets 13 votes out of 100
### if Region 2 comes Candidate A gets 65 votes and Candidtate B gets 35 votes out of 100
### if Region 3 comes Candidate A gets 17 votes and Candidtate B gets 83 votes out of 100
### Here random function calculates regoin 1,2,3 randomly through randint()
import random
def election_result():
    prob1=0
    prob2=0
    region=random.randint(1,3)
    if region==1:
        prob1=prob1+87
        prob2=prob2+13
    elif region==2:
        prob1=prob1+65
        prob2=prob2+35
    else:
        prob1=prob1+17
        prob2=prob2+83
    return prob1,prob2
vote_count_A=0
vote_count_B=0
for r in range(10_000):
    a,b=election_result()
    vote_count_A=vote_count_A+a
    vote_count_B=vote_count_B+b
print(f"Candidate A got {vote_count_A} votes and Candidate B got {vote_count_B} votes!!")
if vote_count_A>vote_count_B:
    print("Candidate A won the election!!")
elif vote_count_A<vote_count_B:
    print("Candidate B won the election!!")
else:
    print("Election was a draw!!")