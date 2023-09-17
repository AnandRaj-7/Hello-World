########## "9.4 Challenge : list of lists" ############
def enrollment_stats(univ):
    enrollment_count = list()
    tuition_fee_details = list()
    for row in range(0,len(univ)):
        enrollment_count.append(univ[row][1])
        tuition_fee_details.append(univ[row][2])
    return enrollment_count, tuition_fee_details
def mean(list1):
    return sum(list1)/len(list1)
def median(list1):
    list1.sort()
    mid = len(list1)//2
    if len(list1) % 2 == 0:
        return (list1[mid-1] + list1[mid])/2
    else:
        return list1[mid]
universities = [ \
['California Institute of Technology', 2175, 37704],\
['Harvard', 19627, 39849],\
['Massachusetts Institute of Technology', 10566, 40732],\
['Princeton', 7802, 37000],\
['Rice', 5879, 35551],\
['Stanford', 19535, 40569],\
['Yale', 11701, 40500]\
]
list1, list2 = enrollment_stats(universities)
print("******************************")
print(f"Total students:    {sum(list1):,}")
print(f"Total tuition : $ {sum(list2):,}")
print(f"\nStudent mean  :    {mean(list1):,.2f}")
print(f"Student median:    {median(list1):,}")
print(f"\nTuition mean  : $  {mean(list2):,.2f}")
print(f"Tuition median: $  {median(list2):,}")
print("******************************")