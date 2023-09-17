from PyPDF2 import PdfReader, PdfWriter
path = "C:/Users/anand/Downloads/Pride-and-Prejudice.pdf"
input_pdf = PdfReader(path)
output_pdf = PdfWriter()
#input_pdf = PdfFileReader(path)

# Printing basic details like title, author, number of pages in the PDF file

print(f"The title of the file is {input_pdf.metadata.title}")
print(f"The author of the file is {input_pdf.metadata.author}")
print(f"The total number of pages in the file is {len(input_pdf.pages)}")
# Extracting the full text of the file in to a text file

with open("The Whistling Gypsy.txt","w") as output_file:
    output_file.write(f"Title : {input_pdf.metadata.title}")
    output_file.write(f"\nAuthor : {input_pdf.metadata.author}")
    output_file.write(f"\nThe number of pages : {len(input_pdf.pages)}\n")
    for page in input_pdf.pages:
        text = page.extract_text()
        #print(text)
        output_file.write(text)
        
# Creating a new PDF file from contents of an old pdf file accept its cover page

with open("The Whistling Gypsy.pdf","wb") as output_file:
    for page in input_pdf.pages:
        if input_pdf.get_page_number(page) == 0:
            continue
        output_pdf.add_page(page)
        output_pdf.write(output_file)