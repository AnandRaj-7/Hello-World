import os
from PyPDF2 import PdfReader, PdfWriter
path = "C:/Users/anand/Downloads"
# 1
input_file_path = os.path.join(path, "The Emperor.pdf")
input_pdf = PdfReader(input_file_path)
output_pdf = PdfWriter()
# 2
watermark_file_path = os.path.join(path, "top_secret.pdf")
watermark_pdf = PdfReader(watermark_file_path)
watermark_page = watermark_pdf.pages[0]
# 3
for page in input_pdf.pages:
    page.merge_page(watermark_page)
    output_pdf.add_page(page)
# 4
output_file_path = os.path.join(path, "New Suit.pdf")
with open(output_file_path, "wb") as output_file:
    output_pdf.write(output_file)