import PyPDF2 as pdf
from io import StringIO
import spacy
import fnmatch,re

file = open('wp\\wp\\313264.pdf', 'rb')
pdf_reader = pdf.PdfFileReader(file)
nlp = spacy.blank("en")


numofpages = pdf_reader.getNumPages()
doc = ""
for i in range(numofpages):
    page = pdf_reader.getPage(i)
    print(page.extractText().upper())
    if ("RESPONDENT" or "RESPONDENTS") in page.extractText().upper():
        doc += page.extractText().upper().replace("(2)", "")
        break
print(doc)

pos1 = doc.replace("VERSUS", "VS").find("VS")
pos2 = doc.replace("RESPONDENTS", "RESPONDENT").find("RESPONDENT", pos1)
print(pos1)
doc = doc[pos1:pos2]
print(doc)

doc = doc.strip().replace("VS", "").replace("-", "").replace("//", "").replace("...", "").replace("..", "").replace("S.", "")

buf = StringIO(doc)
li = buf.readlines()
for i in range(len(li)):
    li[i] = li[i].strip().replace("\n", "")
print(li)
lc = 0
if "." in li[0]:
    li.remove(li[0])
#print(len(li[0]))
if len(li[0]) == 0:
    li.remove(li[0])
#print(li)
if "1" in li[0]:
    imls = []
    iml = ""
    for i in range(len(li)):
        if i == 0:
            iml = ""
            lc+=1
            iml = li[i].strip()
        else:
            if str(lc+1) in li[i][0]:
                imls.append(iml)
                iml = li[i].strip()
                lc+=1
            else:
                iml += li[i].strip()
    imls.append(iml.strip())
    li = imls
else:
    for i in range(len(li)-1):
        li[0] += f' {li[i+1].strip()}'
    li = [li[0].strip()]
print(li)
"""
pos1 = page1.extractText().upper().find("CORAM")
pos2 = page1.extractText().upper().replace("VERSUS", "VS").find("VS", pos1)

doc = page1.extractText().upper()
doc = doc[pos1:pos2]

pattern = "OF\s+\d{4}"

buf = StringIO(doc)
li = buf.readlines()

for i in range(len(li)):
    #print(i, li[i])
    #print(li[i])
    matches = re.findall(pattern, li[i].strip())
    if matches == []:
        continue
    else:
        v=i+1

petApp_list = li[v:]
#print(petApp_list)
for i in range(len(petApp_list)):
    petApp_list[i] =  petApp_list[i].strip().replace("...", "").replace("-", "").replace("..", "").replace("PETITIONERS", "").replace("PETITIONER", "").replace("APPELLANTS", "").replace("APPELLANT", "").replace("…", "").strip()
#print(petApp_list)

lc = 0

if "1" in petApp_list[0]:
    imls = []
    iml = ""
    for i in range(len(petApp_list)):
        if i == 0:
            iml = ""
            lc += 1
            iml = (petApp_list[i])
        else:
            if str(lc+1) in petApp_list[i]:
                imls.append(iml)
                iml = (petApp_list[i])
                lc += 1
            else:
                iml += petApp_list[i].strip().replace("...", "")
    imls.append(iml)
    petApp_list = imls
else:
    for i in range(len(petApp_list)-1):
        petApp_list[0]+=f'{petApp_list[i+1]}'
    petApp_list = [petApp_list[0]]
print(petApp_list)"""



"""for i in range(len(petApp_list)):
    if "1" in petApp_list[i]:
        print(petApp_list[i])"""













"""for i in pattern:
    matches = re.findall(i, doc)"""



"""
#print(li)
#for i in range(len(li)):
    if i%2 == 0:
        print(li[i].replace("\n", ""))
    #print(li[i])"""

"""
if len(li) > 2:
    print(li[0])
    print(li[2])
else:
    print(li[0])
"""



