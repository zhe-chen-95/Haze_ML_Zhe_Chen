__author__= "zyzhang"

import xlrd
import xlwt
import os

inpath="E:\\Haze\\AirObsData\\07\\"
outpath="E:\\Haze\\AirObsData_Trans\\07\\"
os.chdir(inpath)

files=os.listdir()
for file in files:
    ft=open(file,"r",encoding="utf-8")
    wb=xlwt.Workbook()
    ws1 = wb.add_sheet("Sheet1")
    i=0
    for line in ft.readlines():
        j=0
        for item in line.split('\t'):
            ws1.write(i,j,item)
            j=j+1
        i=i+1
    ft.close()
    wb.save(outpath+str(file[:-4])+'.xls')
