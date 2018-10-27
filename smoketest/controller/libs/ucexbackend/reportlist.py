#coding:utf-8
'''
title:  测试执行数据复用
author:Robert
date:20180820
email:shuibo.luo@ucextech.com
other:
'''


class ReportList():
    '''
    关于已生成的报告的查询处理
    '''
    def __init__(self,limit=10):
        self.__limit = limit
    def queryreport(self):
        reportlist =[]
