for i in range (1,10):
    str1 = "*"
    str1 = i*str1
    print(str1)
for i in range (1,10):
    spc = " "
    spc = " "*(9-i)
    str1 = "*"
    str1 = i*str1
    pr_str = spc + str1
    print(pr_str)
for i in range (1,10):
    spc = " "
    str1 = "*"
    str2 = "*"
    str1 = i*str1
    if i == 1:
       pr_str = spc*(9-1) + str2
    else:
        pr_str = spc*(9-i) + str1 + str2*(i-1)
    print(pr_str)
for i in range (1,10):
    str1 = "*"
    str1 = str1*(10-i)
    print(str1)
for i in range (1,10):
    str1 = "*"
    spc = " "
    str1 = str1*(10-i)
    if i == 1 :
        pt_str = str1
    else : 
        pt_str = spc*(i-1) + str1
    print(pt_str)
for i in range (1,10):
    str1 = "*"
    str2 = "*"
    spc = " "
    if i == 1:
        pt_str = str1*(10-i) + str2*(9-i)
    else:
        pt_str = spc*(i-1) + str1*(10-i) + str2*(9-i)
    print(pt_str)