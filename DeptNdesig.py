import PyPDF2 as pdf
import spacy
from io import StringIO

nlp = spacy.load("en_core_web_lg")
file = open("sample.pdf", "rb")

pdf_reader = pdf.PdfFileReader(file)

num_of_pages = pdf_reader.getNumPages()

#print(num_of_pages)
data = [pdf_reader.getPage(i) for i in range(num_of_pages)]
"""for i in range(len(data)):
    print(data[i].extractText())"""
dept = []
for i in data:
    #print(i.extractText().strip())
    doc = nlp(i.extractText())
    buf = StringIO(i.extractText())
    #print(doc)
    #doc2 = nlp(StringIO(i.extractText()))
    #print(doc2)
    for entity  in doc.ents:
        print(entity.text, entity.label_)
        if entity.label_ == "ORG" and "Department" in entity.text.replace("\n", ""):
            #print(entity.text)
            dept.append(entity.text.replace("\n", ""))


print(dept)
