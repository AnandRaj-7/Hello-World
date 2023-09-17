import copy
import os
from PyPDF2 import PdfReader, PdfWriter
path = "C:/Users/anand/Downloads/half_and_half.pdf"
# 1
input_pdf = PdfReader(path)
output_pdf = PdfWriter()

# 2
for page_num in range(0, len(input_pdf.pages)):
    page_left = input_pdf.pages[page_num]
    #print(page_left)
    page_right = copy.copy(page_left)
    #print(page_right)
# Calculate the new coordinates for the upper-right
# corner of the page_left and the upper-left
# corner of page_right
    upper_right = page_left.mediabox.upper_right
    print(upper_right)
    new_coords = (upper_right[0]/2, upper_right[1])
    print(new_coords)
# Crop and add left-side page to the ouput fileṇ
    page_left.mediabox.upper_right = new_coords
    output_pdf.add_page(page_left)
# Crop and add right-side page to the output file
    page_right.mediabox.upper_left = new_coords
    output_pdf.add_page(page_right)
# 3
with open("The Little Mermaid.pdf", "wb") as output_file:
    output_pdf.write(output_file)