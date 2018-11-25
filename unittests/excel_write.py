#!coding=utf-8
##保存数据到excel

import numpy
import pandas
import xlrd
import xlwt

path= "D:\\PyCharm\\bigdata\\"
wb  =xlwt.Workbook()




ws_1 =wb.add_sheet("first_sheet",cell_overwrite_ok=True)
print("get_active_sheet  ",wb.get_active_sheet)
ws_2 = wb.add_sheet('second_sheet')

data = numpy.arange(1,65).reshape((8,8))

print(data)


# ws_1.write(0,0,100)

for c in range(data.shape[0]):
    ###以列为轴  c代表列
    # print("c",c)
    # print("data.shape[0]",data.shape[0])
    for r in range(data.shape[1]):
        ### 以行为轴  r 代表行
        ws_1.write(r,c,str(data[c,r]))
        ws_2.write(r,c,str(data[r,c]))


# for x in range(0,10):
#     print(x)
#     for r in range (0,10):
#         ws_1.write(x,r,'a')
#         ws_2.write(r,x,'b')

# wb.save(path+'workbook.xls')
wb.save(path+'workbook.csv')


