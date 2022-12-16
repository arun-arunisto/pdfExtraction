import re
import PyPDF2 as pdf
import spacy
from io import StringIO


def dataClean(listOfCom, dataToClean):
    for i in listOfCom:
        dataToClean = dataToClean.replace(i, "")
    return dataToClean

def courtDate(start, end, page, document):
    start_pos = page.extractText().upper().replace("RESERVED", "DATE").find(start)
    print(start_pos)
    end_pos = page.extractText().upper().replace("C O R A M", "CORAM").find(end, start_pos)
    print(end_pos)
    data = document[start_pos:end_pos]
    data = data.replace("/", "-")
    data = data.replace(".", "-")
    junklistofDate = ["DATE", "D", ":", " ", "\n", "A", "B", "C", "D", "E", "F", "G", \
                      "H", "I", "J", "K", "L", "M", "N", "O", \
                       "Q", "R", "S", "T", "U", "V", "W", "X", "Y", "Z"]
    data = dataClean(junklistofDate, data)
    data = data.replace("P", " ")
    return data

def judgeName(start, end, page, document, judgenames=[]):
    start_pos = page.extractText().upper().find(start)
    end_pos = page.extractText().upper().find(end, start_pos)
    buf = StringIO(document[start_pos:end_pos])
    li = buf.readlines()
    #print(li)
    for i in range(len(li)):
        li[i] = li[i].replace("---", "").strip()
    """for i in range(len(li)):
        if ("NO" or "AND") not in li[i]:
            print("IF : ",li[i])
        else:
            print("ELSE : ",li[i])"""
    n = "1234567890"
    pattern = "\d"
    #print(li)
    #print(i)
    if re.findall(pattern, li[i])[0]:
        li.remove(li[i])
    #print(li)
    pattern = "\d"
    for i in li:
        for j in range(len(re.findall(pattern, i))):
            if len(re.findall(pattern, i)) != 0:
                try:
                    if (re.findall(pattern, i)[j] in i):
                        print(i)
                        li.remove(i)
                except ValueError:
                    pass
        if (i == ''):
            li.remove(i)
    #print(li)
    for i in li:
        #if re.findall(pattern, li[i]) not in i:
        if (("AND") != i) and (("NO.") not in i):
           judgenames.append(i)

    return judgenames

def courtNos(start, end, page):
    start_pos = page.extractText().upper().find(start)
    end_pos = page.extractText().upper().find(end, start_pos)
    document = page.extractText().upper()
    document = document[start_pos:end_pos]
    pattern = "OF\s+\d{4}"
    buf = StringIO(document)
    li = buf.readlines()
    courtno = []
    for i in range(len(li)):
        matches = re.findall(pattern, li[i].strip())
        if matches == []:
            continue
        courtno.append(li[i].strip())
    for i in range(len(courtno)):
        if courtno[i][0:4] == "AND ":
            courtno[i] = courtno[i].replace(courtno[i][0:4], "")
    return courtno

def PetAppDetails(start, end, page):
    #print(page.extractText())
    start = page.extractText().upper().replace("C O R A M", "CORAM").find(start)
    #print(start)
    end = page.extractText().upper().replace("VERSUS", "VS").find(end, start)
    doc = page.extractText().upper()
    doc = doc[start:end]
    #print(doc)
    buf = StringIO(doc)
    li = buf.readlines()
    #print(li)
    pattern = "OF\s+\d{4}"
    for i in range(len(li)):
        matches = re.findall(pattern, li[i].strip())
        if matches == []:
            continue
        else:
            v=i+1
    petApp_list = li[v:]
    #print(petApp_list)
    junklistAddress = ["...", "-", "..", "PETITIONERS", "PETITIONER", "APPELLANTS", "APPELLANT", "…"]
    for i in range(len(petApp_list)):
        petApp_list[i] = dataClean(junklistAddress, petApp_list[i].strip())
    lc = 0
    print(petApp_list)
    if "1" in petApp_list[0]:
        imls = []
        iml = ""
        for i in range(len(petApp_list)):
            #print(i, lc)
            if i == 0:
                iml = ""
                lc+=1
                iml = (petApp_list[i].strip())
            else:
                #print(petApp_list)
                #print(str(lc + 1))
                #print(petApp_list[i])
                if str(lc+1) in petApp_list[i][0]:
                    imls.append(iml)
                    iml = (petApp_list[i].strip())
                    lc+=1
                else:
                    iml += f' {petApp_list[i].strip()}'
        imls.append(iml.strip())
        petApp_list = imls
    else:
        for i in range(len(petApp_list)-1):
            petApp_list[0]+=f'{petApp_list[i+1].strip()}'
        petApp_list = [petApp_list[0].strip()]
    return petApp_list

def respondentList(start, end, pdfReader):
    numofpages = pdfReader.getNumPages()
    #print(numofpages)
    doc = ""
    for i in range(numofpages):
        page = pdfReader.getPage(i)
        #print(i, page.extractText())
        if ("RESPONDENT" or "RESPONDENTS") not in page.extractText().upper():
            doc += page.extractText().upper()
        else:
            doc += page.extractText().upper()
            break
    start = doc.replace("VERSUS", "VS").replace("V.", "VS").find(start)
    #print(start)
    end = doc.replace("RESPONDENTS", "RESPONDENT").find(end, start)
    doc = doc[start:end]
    #print(doc)
    junkListofRespondent = ["VS", "-", "//", "...", "..", "[", "]"]
    doc = dataClean(junkListofRespondent, doc.strip())
    #print(doc)
    buf = StringIO(doc)
    resList = buf.readlines()
    #print(resList)
    for i in range(len(resList)):
        resList[i] = resList[i].replace("\n", "").strip()
    lc = 0
    #print(resList)
    try:
        if "." in resList[0]:
            resList.remove(resList[0])
        if len(resList[0]) == 0:
            resList.remove(resList[0])
        if "1" in resList[0]:
            imls = []
            iml = ""
            for i in range(len(resList)):
                if i == 0:
                    iml = ""
                    lc+=1
                    iml = resList[i].strip()
                else:
                    if str(lc+1) in resList[i][0]:
                        imls.append(iml)
                        iml = resList[i].strip()
                        lc+=1
                    else:
                        iml+=resList[i].strip()
            imls.append(iml.strip())
            resList = imls
        else:
            for i in range(len(resList)-1):
                resList[0] += f' {resList[i+1].strip()}'
            resList = [resList[0].strip()]
        return resList
    except Exception as e:
        return e





file = open('wp\\wp\\650019.pdf', 'rb')
pdf_reader = pdf.PdfFileReader(file)
nlp = spacy.blank("en")

page1 = pdf_reader.getPage(0)
doc = page1.extractText()
doc = doc.upper()

judges = judgeName("THE HON", "OF", page1, doc)
#print(judges)

"""
judges = judgeName("THE HON", "OF", page1, doc)
print(judges)
date = courtDate("DATE", "CORAM", page1, doc)
print(date)

respondentlist = respondentList("VS", "RESPONDENT", pdf_reader)
print(respondentlist)
name = judges[-1]
no = name.find("JUSTICE")
#print(judges[-1][no:])
court = courtNos("CORAM", "VS", page1)
print(court)
petAppDetails = PetAppDetails("CORAM", "VS", page1)
print(petAppDetails)
petAppDetails = PetAppDetails("CORAM", "VS", page1)
print(petAppDetails)
"""