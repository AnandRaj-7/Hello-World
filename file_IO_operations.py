file = open("Poem.txt",'r')
output_lines = file.readlines()
print("\nPrinting contents in simple way :\n")
for line in output_lines:
    print(line, end = "")
file.close()
## Using with key word##
print("\n\nOutput using with key word :\n")
with open("Poem.txt", 'r') as file:
    for line in file:
        print(line, end = "")
### Opening Poem.txt in read mode and Output.txt in write mode ####
file = open("Poem.txt",'r')
output_file = open("Output.txt", 'w')
output_lines = file.readlines()
for line in output_lines:
    output_file.write(line)
file.close()
output_file.close()
### Opening Poem.txt in read mode and Output.txt in write mode using with key word####
with open("Poem.txt", 'r') as source, open("Output.txt", 'w') as destination:
    for line in source:
        destination.write(line)
with open("Output.txt",'a') as dest:
    dest.write("\nThis is a test line in append mode")