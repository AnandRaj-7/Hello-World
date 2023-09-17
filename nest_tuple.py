data = ((1,2),(3,4))
for i in range(0,len(data)):
    sum1 = sum((data[i]))
    print(f"Row {i+1} sum: {sum1}")
numbers = [4,3,2,1]
copy_numbers = numbers[:]
print(f"The numbers list is: {numbers}")
print(f"The copy of the numbers list is: {copy_numbers}")
numbers.sort()
print(f"Sorted numbers list is: {numbers}")
print(f"The copy of the numbers list is still: {copy_numbers}")