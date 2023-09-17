### This program prints all the number between 1 and 50 which are not the multiples of 50
for x in range (1,50):
    if 50%x==0:
        continue
    else:
        print(f"{x} is not a multiple of 50!")