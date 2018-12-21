# coding:utf-8
'''
title:逻辑控制模块   control
author:Robert
date:20171115
email:robert_luo1949@163.com
'''

import unittest


from qaplatform.testcases.examples_100 import test_example

class ExampleModelSuite(unittest.TestSuite):
    '''
    组织example测试模型
    '''

    def SuiteMulti(self):
        '''
        :
        :return: suitTest
        '''
        # suitepay=payteston.payTest()
        # print('pay', suitepay)
        # ##加载支付的测试脚本
        # suitecontract=contractteston.contractTest()                ##加载支付的测试脚本
        # print('suitecontract',suitecontract)
        # suitTest=unittest.TestSuite((suitepay,suitecontract))  ##把多个脚本合并到一个测试套件testsuite

        suitTest = unittest.TestSuite()

        suitTest.addTests(unittest.makeSuite(test_example.TestStringMethods))         ####example


        return suitTest
