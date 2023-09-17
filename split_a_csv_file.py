##### 11.6 Challenge: Split a CSV file #####
import argparse
import os
import csv
parser = argparse.ArgumentParser()
parser.add_argument('-i', type = str, default="input.csv", help = "Enter the file name in csv format e.g: 'abc.csv'")
parser.add_argument('-o', type = str, default= "output", help = "Enter the file name for output e.g 'xyz'")
parser.add_argument('-r', type = int, default = 100, help = "Enter the number of rows each output file must have")
arg = parser.parse_args()
with open(arg.i, 'r') as csv_file:
    rdr = csv.reader(csv_file)
    data = list()
    for row in rdr:
        data.append(row)
j = len(data)
rows = arg.r
if (j % rows == 0):
    nof = j / rows
else:
    nof = j//rows + 1
count = 1
for nos in range(0,nof):
    with open(arg.o+str(nos)+'.csv','w', newline = '') as output:
        wrt = csv.writer(output)
        wrt.writerow(data[0])
        for i in range(1,rows+1):
            if(count<j):
                wrt.writerow(data[count])
            else:
                break
            count = count + 1