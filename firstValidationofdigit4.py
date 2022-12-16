import PyPDF2 as pdf
from io import StringIO
import spacy
import fnmatch, re
import os
import shutil

"""file = open('documents\\documents\\HCMA011905052022_10.pdf', "rb")
pdf_reader = pdf.PdfFileReader(file)"""
"""
#petitioner
page = pdf_reader.pages[0]
page = page.extractText().strip()
print(page.split())
buf = StringIO(page)
li = buf.readlines()
#print(li, sep=",")
for i in li:
    pass
    #print(i[0])
"""
a = os.listdir("documents\\documents\\")
count = 0
src_path = r'documents\\documents\\'
dest_path = r'firstValidationOFdigit4\\'
#print(a)
for i in a:
    file = open(f'documents\\documents\\{i}', "rb")
    pdf_reader = pdf.PdfFileReader(file)
    page = pdf_reader.pages[0]
    page = page.extractText().upper().strip()
    buf = StringIO(page)
    li = buf.readlines()
    li = li + [i]
    #print(li)
    pattern = "OF\s+\d{4}"
    pattern2 = ".pdf"
    for j in range(len(li)):
        matches = re.findall(pattern, li[j])
        #print(matches)
        if matches == []:
            continue
        else:
            count+=1
            shutil.copy(f'{src_path}{li[-1]}', f'{dest_path}{li[-1]}')
            print("Success", count)
            #print(li[j], li[-1])

print(count)
print(len(a))

