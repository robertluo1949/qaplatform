# -*- coding: utf-8 -*-
# @Time    : 2018/11/25 19:00
# @Author  : Aries
# @Site    : 
# @File    : findlatestfile.py
# @Software: PyCharm

import os
def findlatestfiel():
    '''

    :return:
    '''

    dir = "D:\\Coding\\qaplatform\\tmp\\reports"
    file_lists = os.listdir(dir)
    # mod_time = os.path.getmtime(file_lists)
    print(file_lists)
    # file_lists.sort(key=lambda fn:os.path.getmtime(dir+"\\"+fn))
    file_lists.sort(key=lambda fn:os.path.getmtime(dir+"\\"+fn))

    print(file_lists)
    print("latest modify file：",file_lists[-1])

findlatestfiel()