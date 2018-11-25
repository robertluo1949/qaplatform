# coding:utf-8
'''
title:逻辑控制模块   control
author:Robert
date:20171115
email:robert_luo1949@163.com
'''

import unittest


from qaplatform.testcases.exchange_104 import test_orderceate,\
    test_currentquery,test_orderswithTotalRecordsCountquery,test_dealsfind,test_getoraderid
from qaplatform.testcases.userlogin_101 import test_login,\
    test_captcha,test_forget_changepasswd,test_forget_effective,test_forget_notice,test_phonecode,test_register,test_verify_captcha
from qaplatform.testcases.c2c_103  import test_c2c_boundary, test_c2c_listed, \
    test_c2c_recently,test_c2c_trend,test_c2c_query_orders,test_c2c_get_detail,\
    test_c2c_get_trade_message,test_1c2c_dealer_create,test_c2c_isdealer,test_c2c_remind,test_c2c_user_buy,test_c2c_user_cancle_trade,\
    test_c2c_user_confirmpaied_trade,test_c2c_user_create_trade
from qaplatform.testcases.homepage_102 import test_all_coins,\
    test_hotcoin_list,test_internationals,test_markets_all,test_markets_allcurrencies,test_pc_banner,test_tiker,test_user_markets,test_user_profile



class SmokeModelSuite(unittest.TestSuite):
    '''
    组织ucex smoke测试模型
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

        suitTest.addTests(unittest.makeSuite(test_login.User_login))         ####UCEX  PC的userlogin 101 接口
        suitTest.addTests(unittest.makeSuite(test_captcha.User_captcha))
        suitTest.addTests(unittest.makeSuite(test_forget_notice.User_forgetnotice))
        suitTest.addTests(unittest.makeSuite(test_forget_changepasswd.User_forget_changepasswd))
        suitTest.addTests(unittest.makeSuite(test_forget_effective.User_forgeteffective))
        suitTest.addTests(unittest.makeSuite(test_forget_notice.User_forgetnotice))
        suitTest.addTests(unittest.makeSuite(test_phonecode.User_phonecode))
        suitTest.addTests(unittest.makeSuite(test_register.User_register))
        suitTest.addTests(unittest.makeSuite(test_verify_captcha.User_verifycaptcha))

        suitTest.addTests(unittest.makeSuite(test_all_coins.Homepage_all_coins))   ####UCEX  PC的homepage 102 接口
        suitTest.addTests(unittest.makeSuite(test_hotcoin_list.Homepage_hotcoins_list))
        suitTest.addTests(unittest.makeSuite(test_internationals.Homepage_international))
        suitTest.addTests(unittest.makeSuite(test_markets_all.Homepage_markets_all))
        suitTest.addTests(unittest.makeSuite(test_markets_allcurrencies.Homepage_markets_allcurrencies))
        suitTest.addTests(unittest.makeSuite(test_pc_banner.Homepage_banner))
        suitTest.addTests(unittest.makeSuite(test_tiker.tiker_24h))
        suitTest.addTests(unittest.makeSuite(test_user_markets.Homepage_user_markets))
        suitTest.addTests(unittest.makeSuite(test_user_profile.Homepage_user_profile))

        suitTest.addTests(unittest.makeSuite(test_c2c_boundary.C2C_boundary))  ####UCEX  PC的c2c 103法币买卖接口
        suitTest.addTests(unittest.makeSuite(test_c2c_listed.C2C_listed))
        suitTest.addTests(unittest.makeSuite(test_c2c_trend.C2C_trend))
        suitTest.addTests(unittest.makeSuite(test_c2c_recently.C2C_recently))
        suitTest.addTests(unittest.makeSuite(test_c2c_query_orders.C2C_queryOrders))
        suitTest.addTests(unittest.makeSuite(test_c2c_get_detail.C2C_detail))
        suitTest.addTests(unittest.makeSuite(test_c2c_get_trade_message.C2C_trademessage))
        suitTest.addTests(unittest.makeSuite(test_1c2c_dealer_create.C2C_dealer_create))    ##商家挂单
        suitTest.addTests(unittest.makeSuite(test_c2c_isdealer.C2C_isdealer))
        suitTest.addTests(unittest.makeSuite(test_c2c_remind.C2C_remind))
        suitTest.addTests(unittest.makeSuite(test_c2c_user_buy.C2C_Buy))
        suitTest.addTests(unittest.makeSuite(test_c2c_user_cancle_trade.C2C_cancle_trade))
        # suitTest.addTests(unittest.makeSuite(test_c2c_user_confirmpaied_trade.C2C_confirm_trade))
        suitTest.addTests(unittest.makeSuite(test_c2c_user_create_trade.C2C_create_trade))


        suitTest.addTests(unittest.makeSuite(test_orderceate.ExchangeOrder))         ####UCEX  PC的exchange 104币币交易接口
        suitTest.addTests(unittest.makeSuite(test_orderswithTotalRecordsCountquery.withTotalRecordsCount))
        suitTest.addTests(unittest.makeSuite(test_currentquery.withTotalRecordsCountcurrent))
        suitTest.addTests(unittest.makeSuite(test_dealsfind.tradesdealsfind))
        suitTest.addTests(unittest.makeSuite(test_getoraderid.getorderidquery))


        return suitTest
