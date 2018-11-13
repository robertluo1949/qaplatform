###
### 目标： 采用 开源xlsxwriter 包来进行写入excel
import numpy
from xlsxwriter import  Workbook

PATH= "D:\\PyCharm\\bigdata\\"
wb = Workbook(PATH+"workbook_write.xlsx")
# workbook(PATH+"workbook.xlsx")


ws_1 =wb.add_worksheet("firstsheet")
ws_2 =wb.add_worksheet("secondsheet")

data = numpy.arange(1,82).reshape(9,9)

for c in range(data.shape[0]):

    for r in range(data.shape[1]):
        ws_1.write(c,r,data[c,r])
        ws_2.write(c,r,data[r,c])

wb.close()
