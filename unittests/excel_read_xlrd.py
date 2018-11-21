from xlrd import open_workbook

PATH = "D:\\PyCharm\\bigdata\\"
book = open_workbook(PATH+"workbook_read_xlrd.xls")

print(book.sheet_names())

sheet_1 = book.sheet_by_name("first_sheet")
sheet_2 = book.sheet_by_name("second_sheet")

print(sheet_2.cell(0,0))

print("cols: " ,sheet_2.row(1))


a= sheet_1.row(2)
print("list a :",a)

for c in range(sheet_1.ncols):
    for r in range(sheet_1.nrows):
        pass
    print( '%i' % sheet_1.cell(r,c).value )

##显示一行中的A列----B列
print("Start Col ---End Col ",sheet_2.row_values(3,start_colx=1,end_colx=8))
####显示一列中的A行----B行
print("Start Row --- End Row",sheet_2.col_values(3,start_rowx=1,end_rowx=8))