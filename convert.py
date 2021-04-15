from pdf2image import convert_from_path
from os import listdir
import os
from os.path import isfile, join

pdfPath = os.path.dirname(os.path.realpath(__file__))+"\\PDF"
jpegPath = os.path.dirname(os.path.realpath(__file__))+"\\JPEG"
popplerPath = os.path.dirname(os.path.realpath(__file__))+"\\dependencies\\poppler-21.03.0\\Library\\bin\\"

onlyfiles = [f for f in listdir(pdfPath) if isfile(join(pdfPath, f))]
    
for i in onlyfiles:
    if i == ".gitignore": continue
    print(pdfPath+"\\"+i)
    pages = convert_from_path("PDF\\"+i, 500, poppler_path=popplerPath)
    
    pageNumber = 0
    
    fileName=i.split('.')
    fileName.pop()
    fileName = "".join(fileName)
    
    for page in pages:
        pageNumber+=1
        page.save(jpegPath+"\\"+fileName+str(pageNumber)+".jpeg", 'JPEG')
