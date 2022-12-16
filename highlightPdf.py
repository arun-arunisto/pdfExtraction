import fitz

doc = fitz.open('sample.pdf')
#print(doc.page_count) #to get the total pages
#print(doc.metadata) #to find the meta data
#print(doc.get_toc()) #to get the table of contents
#print(doc.load_page(1))

for page in doc:
    text = "Departments"
    text_instances = page.search_for(text)

    for inst in text_instances:
        highlight = page.add_highlight_annot(inst)
        highlight.update()

doc.save("output.pdf", garbage=4, deflate=True, clean=True)