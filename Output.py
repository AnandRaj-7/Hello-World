import os
if not os.path.exists("Output"):
    os.mkdir("Output")
with open("Output/Python.txt" , "w") as new_file:
    new_file.write("I was put here by Python!”")