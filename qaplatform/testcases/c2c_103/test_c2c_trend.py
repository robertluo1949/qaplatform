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
from qaplatform.testdatas.c2c_103 import  data_c2c_trend




##读取配置文件的接口request url  和   request headers
url_login = data_c2c_trend.url_login
token_user = data_c2c_trend.token_user
t_headers_login = data_c2c_trend.t_headers_login
t_headers_logged = data_c2c_trend.t_headers_logged
token_clienttype = data_c2c_trend.token_clienttype

url = data_c2c_trend.url_c2c_trend


class C2C_trend(unittest.TestCase):
    '''
    法币市场价格趋势
    '''

    def setUp(self):
        obj_token = headertoken.PackgingToken(url_login, data_c2c_trend.token_user, data_c2c_trend.t_headers_login, data_c2c_trend.token_clienttype)
        self.token_value = obj_token.gettokenvalue()

    def tearDown(self):
        pass


    def test_No1030401_get_BTC_trend(self):
        """UCEX QA：BTC trend"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_trend.ucex_inputdata[0]
        conf_output_data = data_c2c_trend.ucex_outputdata[0]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_trend.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_trend.t_headers_logged

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


    def test_No1030402_get_ETH_trend(self):
        """UCEX QA：ETH trend"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_trend.ucex_inputdata[1]
        conf_output_data = data_c2c_trend.ucex_outputdata[1]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_trend.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_trend.t_headers_logged

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


    def test_No1030403_get_USDT_trend(self):
        """UCEX QA：USDT trend"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_trend.ucex_inputdata[2]
        conf_output_data = data_c2c_trend.ucex_outputdata[2]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_trend.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_trend.t_headers_logged

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

    def test_No1030404_get_BG_trend(self):
        """UCEX QA：BG trend"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_trend.ucex_inputdata[3]
        conf_output_data = data_c2c_trend.ucex_outputdata[3]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_trend.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_trend.t_headers_logged

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


    def test_No1030405_get_trend_coincode_nonexist(self):
        """UCEX QA：trend, coin code does not exist"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_trend.ucex_inputdata[4]
        conf_output_data = data_c2c_trend.ucex_outputdata[4]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_trend.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_trend.t_headers_logged

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