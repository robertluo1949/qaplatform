# coding:utf-8
'''
title: 自动化测试 UCEX
author:Robert
date:20180504
email:shuibo.luo@ucextech.com
content:  getoraderid 查询order
other:
'''


import json
import unittest
import config
import requests

from smoketest.controller.libs.ucexbackend import headertoken
from smoketest.controller.log import logger
from smoketest.testdatas.exchange_104 import data_getorderid

##读取配置文件的接口request url  和   request headers
url_login = data_getorderid.url_login
token_user = data_getorderid.token_user[1]

t_headers_login = data_getorderid.t_headers_login
t_header_logined =  data_getorderid.t_headers_order
token_clienttype = data_getorderid.token_clienttype




class getorderidquery(unittest.TestCase):
    '''
    java ucex exchange 模块的测试
    '''
    def setUp(self):
        global temp_result
        obj_token =headertoken.PackgingToken(url_login, token_user, t_headers_login, token_clienttype)
        self.token_value =obj_token.gettokenvalue()

    def tearDown(self):
        pass


    def test_No1040501_getorder_NEW(self):
        """UCEX QA：验证币币交易, FILLED订单查询"""

        url = data_getorderid.url_logined + data_getorderid.ucex_inputdata[1]["urlparameter"]
        logger.logger.debug("doding test " + str(self.id()) + " started")
        logger.logger.info("token value "+str(self.token_value))

        data_getorderid.t_headers_order["ucex-web-api-token"] =self.token_value
        t_header = data_getorderid.t_headers_order
        conf_input_data = data_getorderid.ucex_inputdata[1]
        conf_output_data = data_getorderid.ucex_outputdata[1]

        try:
            response_content = requests.get(url, data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
            logger.logger.info("response_output_data  "+str(response_output_data))
        except BaseException as be:
            logger.logger.exception("baseExcetpion  "+str(be)+"  "+str(response_output_data))
        except Exception as e:
            logger.logger.exception("Excetpion "+str(e)+"  "+str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'respones status code  error')
        # self.assertIsNotNone(response_output_data["data"]["trades"],' Current trades is None !! ')


    def test_No1040502_getorder_CANCELED(self):
        """UCEX QA：验证币币交易, CANCELED订单查询"""

        url = data_getorderid.url_logined + data_getorderid.ucex_inputdata[2]["urlparameter"]
        logger.logger.debug("doding test " + str(self.id()) + " started")
        logger.logger.info("token value "+str(self.token_value))

        data_getorderid.t_headers_order["ucex-web-api-token"] =self.token_value
        t_header = data_getorderid.t_headers_order
        conf_input_data = data_getorderid.ucex_inputdata[2]
        conf_output_data = data_getorderid.ucex_outputdata[2]


        try:
            response_content = requests.get(url, data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
            logger.logger.info("response_output_data  "+str(response_output_data))
        except BaseException as be:
            logger.logger.exception("baseExcetpion  "+str(be)+"  "+str(response_output_data))
        except Exception as e:
            logger.logger.exception("Excetpion "+str(e)+"  "+str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'respones status code  error')
        # self.assertIsNotNone(response_output_data["data"]["trades"],' Current trades is None !! ')
        self.assertEqual(response_output_data['data']['orderState'], conf_output_data['data']['orderState'],    'respones status code  error')


    def test_No1040503_getorder_NEW(self):
        """UCEX QA：验证币币交易, NEW订单查询"""

        url = data_getorderid.url_logined + data_getorderid.ucex_inputdata[3]["urlparameter"]
        logger.logger.debug("doding test " + str(self.id()) + " started")
        logger.logger.info("token value " + str(self.token_value))

        data_getorderid.t_headers_order["ucex-web-api-token"] = self.token_value
        t_header = data_getorderid.t_headers_order
        conf_input_data = data_getorderid.ucex_inputdata[3]
        conf_output_data = data_getorderid.ucex_outputdata[3]

        try:
            response_content = requests.get(url, data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
            logger.logger.info("response_output_data  " + str(response_output_data))
        except BaseException as be:
            logger.logger.exception("baseExcetpion  " + str(be) + "  " + str(response_output_data))
        except Exception as e:
            logger.logger.exception("Excetpion " + str(e) + "  " + str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'], 'respones status code  error')
        # self.assertIsNotNone(response_output_data["data"]["trades"],' Current trades is None !! ')
        self.assertEqual(response_output_data['data']['orderState'], conf_output_data['data']['orderState'],
                         'respones status code  error')