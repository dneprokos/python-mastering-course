# python .\10_popular_pyton_packages\9_working_with_pdf.py

from PyPDF2 import PdfReader, PdfWriter
from pathlib import Path

path = Path("10_popular_pyton_packages") / "first.pdf"
print(path)

with open(path, "rb") as file:
    reader = PdfReader(file)
    print(len(reader.pages))

    page = reader.pages[0]  # ✅ modern way to access a page
    page.rotate(90)         # ✅ rotate clockwise by 90 degrees

    writer = PdfWriter()
    writer.add_page(page)   # ✅ new method name

    with open("rotated.pdf", "wb") as output:
        writer.write(output)
