import pdfplumber 

pdf = pdfplumber.open("pdfs/workplace.pdf") 
page = pdf.pages[3]
text = page.extract_text()
print(text)