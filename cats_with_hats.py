##### 9.9 Challenge: Cats With Hats #####
cats = dict()
for i in range (1,101):
    cats[i] = "Hats Off"
print("\nThe original cats dictionary before the exercie is \n\n",cats)
key = 1
for round in range (1,101):
    key = round
    while key <= 100 :
        if cats[key] == "Hats Off" :
            cats[key] = "Hats On"
        else :
            cats[key] = "Hats Off"
        key = key + round
count = 0
print("\nThe cats dictionary after 100 rounds of exercie is \n\n",cats)
for i in range(1,101):
    if cats[i] == "Hats On":
        count += 1
print(f"\nThe number of cats having 'Hats On' after the exercise are {count}\n")