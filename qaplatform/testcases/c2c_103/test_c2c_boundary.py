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

from qaplatform.controller.libs.ucexbackend import headertoken
from qaplatform.controller.log import logger
from qaplatform.testdatas.c2c_103 import  data_c2c_boundary




##读取配置文件的接口request url  和   request headers
url_login = data_c2c_boundary.url_login
token_user = data_c2c_boundary.token_user
t_headers_login = data_c2c_boundary.t_headers_login
t_headers_logged = data_c2c_boundary.t_headers_logged
token_clienttype = data_c2c_boundary.token_clienttype

url = data_c2c_boundary.url_c2c_boundary


class C2C_boundary(unittest.TestCase):
    '''
    法币市场价格和最新价格
    '''

    def setUp(self):
        obj_token = headertoken.PackgingToken(url_login, data_c2c_boundary.token_user, data_c2c_boundary.t_headers_login, data_c2c_boundary.token_clienttype)
        self.token_value = obj_token.gettokenvalue()

    def tearDown(self):
        pass


    def test_No1030201_get_BTC_sell_list(self):
        """UCEX QA：BTC sell list"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_boundary.ucex_inputdata[0]
        conf_output_data = data_c2c_boundary.ucex_outputdata[0]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_boundary.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_boundary.t_headers_logged

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

    def test_No1030202_get_ETH_sell_list(self):
        """UCEX QA：ETH sell list"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_boundary.ucex_inputdata[1]
        conf_output_data = data_c2c_boundary.ucex_outputdata[1]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_boundary.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_boundary.t_headers_logged

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


    def test_No1030203_get_USDT_sell_list(self):
        """UCEX QA：USDT sell list"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_boundary.ucex_inputdata[2]
        conf_output_data = data_c2c_boundary.ucex_outputdata[2]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_boundary.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_boundary.t_headers_logged

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


    def test_No1030204_get_BG_sell_list(self):
        """UCEX QA：BG sell list"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_boundary.ucex_inputdata[3]
        conf_output_data = data_c2c_boundary.ucex_outputdata[3]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_boundary.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_boundary.t_headers_logged

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


    def test_No1030205_get_nonexistcoin_sell_list(self):
        """UCEX QA：get sell list, but coin code does not exist"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_boundary.ucex_inputdata[4]
        conf_output_data = data_c2c_boundary.ucex_outputdata[4]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_boundary.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_boundary.t_headers_logged

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

    def test_No1030206_get_BTC_buy_list(self):
        """UCEX QA：get BTC buy list"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_boundary.ucex_inputdata[5]
        conf_output_data = data_c2c_boundary.ucex_outputdata[5]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_boundary.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_boundary.t_headers_logged

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


    def test_No1030207_get_ETH_buy_list(self):
        """UCEX QA：get ETH buy list"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_boundary.ucex_inputdata[6]
        conf_output_data = data_c2c_boundary.ucex_outputdata[6]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_boundary.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_boundary.t_headers_logged

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

    def test_No1030208_get_USDT_buy_list(self):
        """UCEX QA：get USDT buy list"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_boundary.ucex_inputdata[7]
        conf_output_data = data_c2c_boundary.ucex_outputdata[7]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_boundary.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_boundary.t_headers_logged

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

    def test_No1030209_get_BG_buy_list(self):
        """UCEX QA：get BG buy list"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_boundary.ucex_inputdata[8]
        conf_output_data = data_c2c_boundary.ucex_outputdata[8]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_boundary.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_boundary.t_headers_logged

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

    def test_No1030210_get_BTC_otctype_error_list(self):
        """UCEX QA：get BTC list, but otc type error"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_boundary.ucex_inputdata[9]
        conf_output_data = data_c2c_boundary.ucex_outputdata[9]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_boundary.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_boundary.t_headers_logged

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