# pip install pypiwin32

import win32com.client as win32
import os
path=os.path.dirname(__file__)

excel = win32.gencache.EnsureDispatch('Excel.Application')

files=os.listdir(path)



for file in files:
    if file.endswith('.xls'):

        fname = os.path.join(path,file)
        # print(fname)
        wb = excel.Workbooks.Open(fname)
        new_file_name=os.path.join(path,file.split('.')[0].split('_')[-1])
        # new_file_name=file.split('.')[0].split('_')[-1]
        wb.SaveAs(new_file_name, FileFormat = 51)    #FileFormat = 51 is for .xlsx extension
        wb.Close()
        os.remove(fname)                               #FileFormat = 56 is for .xls extension

excel.Application.Quit()

