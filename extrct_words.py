import pdfplumber 

pdff = pdfplumber.open("pdfs/workplace.pdf")
page = pdff.pages[3]
words = page.extract_words()
print(words)