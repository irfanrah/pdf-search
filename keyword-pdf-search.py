# import packages
import PyPDF2
import re
import os
import warnings
import shutil





def pdf_search(object, target):
    # open the pdf file
    object_PyPDF = PyPDF2.PdfFileReader(object)

    # get number of pages
    NumPages = object_PyPDF.getNumPages()

    # define keyterms
    String = ["arm","Arm"]

    isFinish = False

    for j in range(len(String)):
        if isFinish:
            break 
        for i in range(0, NumPages):
            PageObj = object_PyPDF.getPage(i)
            Text = PageObj.extractText() 
            ResSearch = re.search(String[j], Text)
            if ResSearch is not None:
                isFinish = True
                #print(object)
                shutil.copy(object, os.path.join(target, object))
                break

if __name__ == "__main__":
    warnings.filterwarnings('ignore')
    list_dir = os.listdir("file")
    target = "target"
    for i in list_dir:
        pdf_path = os.path.join("file", i)
        print(pdf_path)
        pdf_search(pdf_path, target)