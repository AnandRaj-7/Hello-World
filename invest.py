def invest(amount,rate,years):
    for year in range(years):
        amount=amount*(1+rate/100)
        print(f"year {year+1}: ${amount:.2f}")
x=float(input("Enter an initial amount: "))
y=float(input("Enter an annual percentage rate: "))
z=int(input("Enter number of years: "))
invest(x,y,z)