__author__= "zyzhang"

import xlrd
import xlwt
import os

inpath="D:\\Haze\\AirObsData\\"
outpath="D:\\Haze\\Trans\\"
os.chdir(inpath)

files=os.listdir()
for file in files:
    ft=open(file,"r",encoding="utf-8")
    wb=xlwt.Workbook()
    ws1 = wb.add_sheet("Sheet1")
    i=0
    for line in ft.readlines():
        j=0
        line_sp=line.split()
        
        for item in line_sp:
            if len(line_sp)==15 and j>=4:
                if j==4:
                    continue
                ws1.write(i,j-1,item)
                j=j+1
                continue
             
           
                
            ws1.write(i,j,item)
            j=j+1
        i=i+1
    ft.close()
    wb.save(outpath+str(file[:-4])+'.xls')
