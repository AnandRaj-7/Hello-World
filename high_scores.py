##### 11.5 Challenge: Create a High Scores List #####
import os
import csv
scores = [["user name", "scores"],
          ["ram","30"],
          ["rajesh","35"],
          ["deepak","17"],
          ["sebastian","20"],
          ["rana","29"],
          ["manoj","11"],
          ["johny","50"],
          ["rana","29"],
          ["johny","60"],
          ["sebastian","25"],
          ["sebastian","40"],
          ["rajesh","30"],
          ["sebastian","25"],
          ["rana","29"],
          ["rana","40"],
          ["ram","32"],
          ["johny","50"],
          ["ram","35"],
          ["rajesh","36"],
          ["deepak","18"],
          ["deepak","20"],
          ["manoj","50"],
          ["deepak","25"],
          ["manoj","48"]]
path = "Output"
with open((os.path.join(path,"scores.csv")), "w", newline = "") as new_file:
    wtr = csv.writer(new_file)
    wtr.writerows(scores)
with open((os.path.join(path,"scores.csv")), "r") as read_file:
    rdr = csv.reader(read_file)
    next(rdr)
    High_scores = {}
    for row in rdr:
        if row[0] in High_scores:
            High_scores[row[0]] = max(High_scores[row[0]],row[1])
        else:
            High_scores[row[0]] = row[1]
sorted_user_list = sorted(High_scores)
print("User : High Scores")
for user in sorted_user_list:
    print(f"{user} : {High_scores[user]}")