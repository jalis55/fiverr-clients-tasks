import openpyxl
import os

path=os.path.dirname(__file__)
files=os.listdir(path)

for file in files:
    if file.endswith('.xlsx'):
        wb=openpyxl.load_workbook(os.path.join(path,file))
        wb_sheet=wb[wb.sheetnames[0]]
        title=file.split('.')[0]

        wb_sheet.title=title
        wb.save(os.path.join(path,file))
        wb.close()
        

