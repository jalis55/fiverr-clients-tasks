import csv
import openpyxl
import os

path=os.path.dirname(__file__)
files=os.listdir(path)

for idx,file in enumerate(files):
    if file.endswith('.txt'):
        fname=os.path.join(path,file)
        wb=openpyxl.Workbook()
        ws=wb.worksheets[0]
        with open(file,'r') as data:
            file_data=csv.reader(data,delimiter="\t")
            for row in file_data:
                ws.append(row)
            output_file=str(idx)+'.xlsx'
            wb.save(os.path.join(path,output_file))
            wb.close()
        os.remove(fname)



