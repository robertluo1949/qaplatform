# -*- coding: utf-8 -*-
import xlrd

FILEPATH = 'D:\PyCharm\bigdata\readexcel.xlsx'



def open_excel(file = FILEPATH):#打开要解析的Excel文件
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception as e:
        print(e)

def excel_by_index(file =FILEPATH , colindex = 0, by_index = 0):#按表的索引读取
    data = open_excel(file)#打开excel文件
    tab = data.sheets()[by_index]#选择excel里面的Sheet
    nrows = tab.nrows#行数
    ncols = tab.ncols#列数
    colName = tab.row_values(colindex)#第0行的值
    list = []#创建一个空列表
    for x in range(0, nrows):
        row = tab.row_values(x)
        if row:
            app = {}#创建空字典
            for y in range(0, ncols):
                app [ colName[y] ] = row[y]
            list.append(app)
    return list

def read_excel(file = FILEPATH, by_index = 0):#直接读取excel表中的各个值
    data = open_excel(file)#打开excel文件
    tab = data.sheets()[by_index]#选择excel里面的Sheet
    nrows = tab.nrows#行数
    ncols = tab.ncols#列数
    for x in range(0, nrows):
         for y in range(0, ncols):
             value = tab.cell(x,y).value
             print(tab.cell(x, y).value)
def main():
    # print('input the path of your file:')
    # a = open_excel(r'D:\smt_ioe\untitled\analysis_excel\my.xls')
    # print(a)
    b = excel_by_index(r'D:\smt_ioe\untitled\analysis_excel\my.xls', 0, 2)
    m = []
    for i in range(b.__len__()):
        c = b[i]
        # a = c['name']
    for x in c:
        if x == 'date':
            print(x)
    print('meng')
    read_excel(r'D:\smt_ioe\untitled\analysis_excel\my.xls',2)

if __name__ == '__main__':
    main()

