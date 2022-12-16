import PyPDF2 as pdf
from io import StringIO
file = open('sample.pdf', 'rb')

pdf_reader = pdf.PdfFileReader(file) #to read and get datas frmm pdf file
pdf_writer = pdf.PdfFileWriter() #its used to add/write or merge pdf's


#print(pdf_reader.pdf_header)
#print(pdf_reader.getNumPages()) #to get number of pages

page1 = pdf_reader.getPage(0) #to get a particular page
#print(page1.extractText()) #to print the content of the page

page2 = pdf_reader.getPage(1)
#print(page2.extractText())
buf = StringIO(page2.extractText())
print(len(buf.readline()))
print(buf.readlines())


#Append/Write PDFs
"""
pdf_writer.addPage(page1)
output = open("Pages.pdf", "wb")
pdf_writer.write(output)
output.close()
"""

#merging two pdf's
"""
pdf_writer.addPage(page1)
pdf_writer.addPage(page2)
output = open('Pages.pdf', "wb")
pdf_writer.write(output)
output.close()
"""
#merging pdf with the pages that yuu want in an order
"""
pdf_writer.addPage(page2)
pdf_writer.addPage(page1)
output = open('Pages.pdf', "wb")
pdf_writer.write(output)
output.close()
"""
#vsualisation

junklistOfAddress = []
junklistofDate = ["DATE", "DATED", ":", " ","\n"]