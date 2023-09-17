import os
import csv
contents = [["Name", "Favorite Pastime"],["Ravi Prakash", "Reading"],["Sonu Ahlawat", "Jogging"],["Deepak Chaurasiya","Talking"],["Ranjita Ranade", "Fighting"],["John Bundy", "Fist Fighting"]]
with open("pastimes.csv", "w", newline = "") as new_file:
    writer = csv.writer(new_file)
    writer.writerows(contents)
with open("pastimes.csv", "r") as read_file:
    reader = csv.reader(read_file)
    next(reader)
    # for row in reader:
    #     print(row)
with open("pastimes.csv", "r") as modify_file:
    rdr = csv.reader(modify_file)
    modify_row_list = list()
    for row in rdr:
        new_row = row
        print(new_row)
        if(row[1].lower().find("fighting")>=0):
            new_row.append("Combat")
            print(new_row)
        else:
            new_row.append("other")
            print(new_row)       
        modify_row_list.append(new_row)
    print(modify_row_list)
with open("pastimes.csv", "w", newline = "") as modified_file:
    wrt = csv.writer(modified_file)
    wrt.writerows(modify_row_list)
with open("pastimes.csv", "r") as modify_file:
    rdr = csv.reader(modify_file)
    modify_new_file = list()
    for row in rdr:
        new_row_in_file = row
        print(new_row_in_file)
        if(row[1].lower().find("favorite pastime")>=0):
            new_row_in_file.append("Type of Pastime")
            print(new_row_in_file)
        elif(row[1].lower().find("fighting")>=0):
            new_row_in_file.append("Combat")
            print(new_row_in_file)
        else:
            new_row_in_file.append("Other")
            print(new_row_in_file)     
        modify_new_file.append(new_row_in_file)
    print(modify_new_file)
with open("pastimes.csv", "r") as modified_file:
    rdr = csv.reader(modified_file)
    modify_new_file = list()
    for row in rdr:
        new_row_in_file = row
        print(new_row_in_file)
        if(row[1].lower().find("favorite pastime")>=0):
            new_row_in_file[2] = "Type of Pastime"
            print(new_row_in_file)
        elif(row[1].lower().find("fighting")>=0):
            new_row_in_file[2] = "Combat"
            print(new_row_in_file)      
        modify_new_file.append(new_row_in_file)
    print(modify_new_file)
path = "Output"
path = os.path.join(path ,"categorized pastimes.csv")
with open(path, "w", newline = "") as modified_file:
    wrt = csv.writer(modified_file)
    wrt.writerows(modify_new_file)