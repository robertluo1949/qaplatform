# coding:utf-8
'''
title: 自动化测试 UCEX
author:Robert
date:20180504
email:shuibo.luo@ucextech.com
content:  java user-order
other:
'''


import json,time
import unittest
import requests
import config

from smoketest.controller.libs.ucexbackend import headertoken
from smoketest.controller.log import logger
from smoketest.testdatas.exchange_104 import data_ordercreate

##读取配置文件的接口request url  和   request headers
url_login = data_ordercreate.url_login
token_user = data_ordercreate.token_user
url_ordercreate = data_ordercreate.url_exchangeorderscreate
t_headers_login = data_ordercreate.t_headers_login
t_header_order = data_ordercreate.t_headers_order
token_clienttype = data_ordercreate.token_clienttype




class ExchangeOrder(unittest.TestCase):
    '''
    java ucex exchange 模块的测试
    '''
    # def __init__(self):
    #     token_value =self.token_value
    #     print("token")
    def setUp(self):
        global temp_result

    def tearDown(self):
        pass


    def test_No1040101_exchangeorderscreate_BUY(self):
        """UCEX QA：验证币币交易, 用户进行买入交易成功"""

        obj_token =headertoken.PackgingToken(url_login, data_ordercreate.token_user[1], data_ordercreate.t_headers_login, token_clienttype)
        self.token_value =obj_token.gettokenvalue()

        logger.logger.debug("doding test " + str(self.id()) + " started")
        logger.logger.info("token value "+str(self.token_value))

        data_ordercreate.t_headers_order["ucex-web-api-token"] =self.token_value
        t_header = data_ordercreate.t_headers_order
        conf_input_data = data_ordercreate.ucex_exchangeorderscreate_inputdata[1]
        conf_output_data = data_ordercreate.ucex_exchangeorderscreate_outputdata[1]


        try:

            response_content = requests.post(url_ordercreate, data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
            logger.logger.info("response_output_data  "+str(response_output_data))
            config.temp_result["No1040101orderId"] =response_output_data['data']["orderId"]
        except BaseException as be:
            logger.logger.exception("baseExcetpion  "+str(be)+"  "+str(response_output_data))
        except Exception as e:
            logger.logger.exception("Excetpion "+str(e)+"  "+str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        self.assertIsNotNone(response_output_data['data'], 'data list is none')

        logger.logger.info(self.id() + "--orderId-- [" + str(response_output_data['data']["orderId"]) + "]")


    def test_No1040102_exchangeorderscreate_SELL(self):
        """UCEX QA：验证币币交易, 用户进行卖出交易成功"""

        obj_token =headertoken.PackgingToken(url_login, data_ordercreate.token_user[2], data_ordercreate.t_headers_login, token_clienttype)
        self.token_value =obj_token.gettokenvalue()
        obj_header =headertoken.PackgingHeaader(data_ordercreate.t_headers_order["Content-Type"], self.token_value)
        logger.logger.debug("doding test " + str(self.id()) + " started")
        logger.logger.info("token value "+str(self.token_value))
        data_ordercreate.t_headers_order["ucex-web-api-token"] =self.token_value
        t_header = data_ordercreate.t_headers_order
        conf_input_data = data_ordercreate.ucex_exchangeorderscreate_inputdata[2]
        conf_output_data = data_ordercreate.ucex_exchangeorderscreate_outputdata[2]

        try:

            response_content = requests.post(url_ordercreate, data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
            logger.logger.info("response_output_data  "+str(response_output_data))

            config.temp_result["No1040102orderId"] = response_output_data['data']["orderId"]
        except BaseException as be:
            logger.logger.exception("baseExcetpion  "+str(be))
        except Exception as e:
            logger.logger.exception("Excetpion "+str(e))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        self.assertIsNotNone(response_output_data['data'], 'data list is none')
        logger.logger.info(self.id()+"--orderId-- ["+str(response_output_data['data']["orderId"])+"]")

    def test_No1040103_exchangeorderscreate_BUY_notenough(self):
        """UCEX QA：验证币币交易, 用户余额不足进行买入交易失败"""

        obj_token_notenough =headertoken.PackgingToken(url_login, data_ordercreate.token_user[3], data_ordercreate.t_headers_login, token_clienttype)
        self.token_value =obj_token_notenough.gettokenvalue()
        logger.logger.debug("doding test " + str(self.id()) + " started")
        logger.logger.info("token value "+str(self.token_value))

        data_ordercreate.t_headers_order["ucex-web-api-token"] =self.token_value
        t_header = data_ordercreate.t_headers_order
        conf_input_data = data_ordercreate.ucex_exchangeorderscreate_inputdata[3]
        conf_output_data = data_ordercreate.ucex_exchangeorderscreate_outputdata[3]

        try:

            response_content = requests.post(url_ordercreate, data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
            logger.logger.info("response_output_data  "+str(response_output_data))

            config.temp_result["No1040103orderId"] = response_output_data['data']["orderId"]
        except BaseException as be:
            logger.logger.exception("baseExcetpion  "+str(be)+"  "+str(response_output_data))
        except Exception as e:
            logger.logger.exception("Excetpion "+str(e)+"  "+str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        self.assertIsNotNone(response_output_data['data'], 'data list is none')

        logger.logger.info(self.id() + "--orderId-- [" + str(response_output_data['data']["orderId"]) + "]")


    def test_No1040104_exchangeorderscreate_SELL_notenough(self):
        """UCEX QA：验证币币交易, 用户余额不足进行卖出交易"""

        obj_token_notenough =headertoken.PackgingToken(url_login, data_ordercreate.token_user[4], data_ordercreate.t_headers_login, token_clienttype)
        self.token_value =obj_token_notenough.gettokenvalue()

        logger.logger.debug("doding test " + str(self.id()) + " started")
        logger.logger.info("token value "+str(self.token_value))

        data_ordercreate.t_headers_order["ucex-web-api-token"] =self.token_value
        t_header = data_ordercreate.t_headers_order

        conf_input_data = data_ordercreate.ucex_exchangeorderscreate_inputdata[4]
        conf_output_data = data_ordercreate.ucex_exchangeorderscreate_outputdata[4]

        try:

            response_content = requests.post(url_ordercreate, data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
            logger.logger.info("response_output_data  "+str(response_output_data))
            config.temp_result["No1040104orderId"] = response_output_data['data']["orderId"]
        except BaseException as be:
            logger.logger.exception("baseExcetpion  "+str(be))
        except Exception as e:
            logger.logger.exception("Excetpion "+str(e))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        self.assertIsNotNone(response_output_data['data'], 'data list is none')

        logger.logger.info(self.id()+"--orderId-- ["+str(response_output_data['data']["orderId"])+"]")

        self.assertEqual(response_output_data['data']['orderState'],conf_output_data['data']['orderState'])