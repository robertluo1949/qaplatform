# coding:utf-8
'''
title: 自动化测试 UCEX
author: bessie
date: 20180917
email:
content:
other:
'''
import json
import unittest

import requests

from smoketest.controller.libs.ucexbackend import headertoken
from smoketest.controller.log import logger
from smoketest.testdatas.c2c_103 import  data_c2c_recently




##读取配置文件的接口request url  和   request headers
url_login = data_c2c_recently.url_login
token_user = data_c2c_recently.token_user
t_headers_login = data_c2c_recently.t_headers_login
t_headers_logged = data_c2c_recently.t_headers_logged
token_clienttype = data_c2c_recently.token_clienttype

url = data_c2c_recently.url_c2c_recently


class C2C_recently(unittest.TestCase):
    '''
    法币市场最近交易列表
    '''

    def setUp(self):
        obj_token = headertoken.PackgingToken(url_login, data_c2c_recently.token_user, data_c2c_recently.t_headers_login, data_c2c_recently.token_clienttype)
        self.token_value = obj_token.gettokenvalue()

    def tearDown(self):
        pass


    def test_No1030801_get_BTC_recent_trades_list(self):
        """UCEX QA：BTC recent trades list"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_recently.ucex_inputdata[0]
        conf_output_data = data_c2c_recently.ucex_outputdata[0]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_recently.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_recently.t_headers_logged

        try:
            response_content = requests.get(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')

        logger.logger.info(self.id())


    def test_No1030802_get_ETH_recent_trades_list(self):
        """UCEX QA：ETH recent trades list"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_recently.ucex_inputdata[1]
        conf_output_data = data_c2c_recently.ucex_outputdata[1]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_recently.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_recently.t_headers_logged

        try:
            response_content = requests.get(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')

        logger.logger.info(self.id())


    def test_No1030803_get_USDT_recent_trades_list(self):
        """UCEX QA：USDT recent trades list"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_recently.ucex_inputdata[2]
        conf_output_data = data_c2c_recently.ucex_outputdata[2]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_recently.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_recently.t_headers_logged

        try:
            response_content = requests.get(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')

        logger.logger.info(self.id())

    def test_No1030804_get_BG_recent_trades_list(self):
        """UCEX QA：BG recent trades list"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_recently.ucex_inputdata[3]
        conf_output_data = data_c2c_recently.ucex_outputdata[3]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_recently.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_recently.t_headers_logged

        try:
            response_content = requests.get(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')

        logger.logger.info(self.id())


    def test_No1030805_get_recent_trades_list_coincode_nonexist(self):
        """UCEX QA：recent trades list, coin code does not exist"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_recently.ucex_inputdata[4]
        conf_output_data = data_c2c_recently.ucex_outputdata[4]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_recently.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_recently.t_headers_logged

        try:
            response_content = requests.get(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')

        logger.logger.info(self.id())