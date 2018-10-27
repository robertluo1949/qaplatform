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
from smoketest.testdatas.c2c_103 import data_c2c_user_buy



##读取配置文件的接口request url  和   request headers
url_login = data_c2c_user_buy.url_login
token_user = data_c2c_user_buy.token_user
t_headers_login = data_c2c_user_buy.t_headers_login
t_headers_logged = data_c2c_user_buy.t_headers_logged
token_clienttype = data_c2c_user_buy.token_clienttype

url = data_c2c_user_buy.url_c2c_user_buy


class C2C_Buy(unittest.TestCase):
    '''
    法币购买-一键匹配
    '''

    def setUp(self):
        obj_token = headertoken.PackgingToken(url_login, token_user,
                                              data_c2c_user_buy.t_headers_login,
                                              data_c2c_user_buy.token_clienttype)
        self.token_value = obj_token.gettokenvalue()

    def tearDown(self):
        pass

    def test_No1030901_buy_BTC_smallerThanMinlimit(self):
        """UCEX QA：buy BTC, but the total money is less than the order's min limit"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_user_buy.ucex_inputdata[0]
        conf_output_data = data_c2c_user_buy.ucex_outputdata[0]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_user_buy.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_user_buy.t_headers_logged

        try:
            response_content = requests.post(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')

        logger.logger.info(self.id())

    def test_No1030902_buy_BTC_biggerThanMaxlimit(self):
        """UCEX QA：buy BTC, but the total money is more than the order's max limit"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_user_buy.ucex_inputdata[1]
        conf_output_data = data_c2c_user_buy.ucex_outputdata[1]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_user_buy.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_user_buy.t_headers_logged

        try:
            response_content = requests.post(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')

        logger.logger.info(self.id())


    def test_No1030903_buy_BTC_cannottrade_toolow(self):
        """UCEX QA：buy BTC, the price is too low, can not trade"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_user_buy.ucex_inputdata[2]
        conf_output_data = data_c2c_user_buy.ucex_outputdata[2]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_user_buy.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_user_buy.t_headers_logged

        try:
            response_content = requests.post(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')

        logger.logger.info(self.id())


    def test_No1030904_buy_BTC_success(self):
        """UCEX QA：buy BTC, success"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_user_buy.ucex_inputdata[3]
        conf_output_data = data_c2c_user_buy.ucex_outputdata[3]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_user_buy.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_user_buy.t_headers_logged

        try:
            response_content = requests.post(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        self.assertIsNotNone(response_output_data['data'],'returned order list is none')

        logger.logger.info(self.id())

    def test_No1030905_buy_coincode_error(self):
        """UCEX QA：buy, but coin code does not exist"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_user_buy.ucex_inputdata[4]
        conf_output_data = data_c2c_user_buy.ucex_outputdata[4]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_user_buy.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_user_buy.t_headers_logged

        try:
            response_content = requests.post(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')

        logger.logger.info(self.id())