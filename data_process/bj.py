
import xlrd
import xlwt
import os

inpath="D:\\Haze\\Trans\\"
outpath="D:\\Haze\\"
os.chdir(inpath)

#Dict for positions of stations
fpos = xlrd.open_workbook("C:\\Users\\Cecil\\Desktop\\zzy\\bj.xlsx")
sheetpos = fpos.sheet_by_index(0)
pos={}
for i in range(12):
    station = sheetpos.cell(i,0).value
    long = float(sheetpos.cell(i,1).value)
    lat = float(sheetpos.cell(i,2).value)
    pos[station]=[long,lat]

files=os.listdir()
#print(files)
fr=xlwt.Workbook() #fileresult
sr=fr.add_sheet("Sheet1") #sheetresult
j = 0
j_j = 0

for file in files:
    print(file)
    year = int(file[2:6])
    month = int(file[6:8])
    day = int(file[8:10])
    hour = int(file[10:12])
    
    fx = xlrd.open_workbook(file)
    sheet = fx.sheet_by_index(0)

 
    for i in range(sheet.nrows):
    #    cityname = sheet.cell(i,11).value
        try:
        
            cityname = sheet.cell(i,0).value
    
            if cityname.find('海淀区万柳')==0:
                    sr.write(j,0,year)
                    sr.write(j,1,month)
                    sr.write(j,2,day)
                    sr.write(j,3,hour)
                    station = sheet.cell(i,0).value
                    long,lat = pos[station]
                    sr.write(j,4,station)
                    sr.write(j,5,long)
                    sr.write(j,6,lat)
                    for k in range(2,11):
                        val = sheet.cell(i,k).value
                        sr.write(j,k+5,val)
                    j = j+1
                    if j==j_j*100:
                        j_j+=1
                        print(file,j)
                
        except:
            print(i,file)
           # input()
fr.save(outpath+"bjresult.xls")

