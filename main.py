from PyPDF2 import PdfWriter

merger = PdfWriter()

PDFS = []
n = int(input("Enter the number of PDFs to merge: "))

for i in range(0, n):
    Name = input(f"Enter the name of PDF {i + 1}: ")
    PDFS.append(Name)

for pdf in PDFS:
    merger.append(pdf)

merger.write("merged.pdf")
merger.close()
print("PDFs merged successfully into 'merged.pdf'.")