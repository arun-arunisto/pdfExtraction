import PyPDF2 as pdf
from io import StringIO
import spacy
import fnmatch, re
import os
import shutil

a = os.listdir("firstValidationOFdigit4\\")
print(len(a))
for i in a:
    file = open(f'documents\\documents\\{i}', "rb")
    pdf_reader = pdf.PdfFileReader(file)
    page = pdf_reader.pages[0]
    page = page.extractText().upper().replace("W.P. NO.", "W.P.NO.").strip()
    print(page)