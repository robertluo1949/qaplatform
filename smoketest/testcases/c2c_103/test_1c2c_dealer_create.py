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
from smoketest.testdatas.c2c_103 import  data_c2c_dealer_create




##读取配置文件的接口request url  和   request headers
url_login = data_c2c_dealer_create.url_login
token_user = data_c2c_dealer_create.dealer_token_user
t_headers_login = data_c2c_dealer_create.t_headers_login
t_headers_logged = data_c2c_dealer_create.t_headers_logged
token_clienttype = data_c2c_dealer_create.token_clienttype

url = data_c2c_dealer_create.url_c2c_dealer_create


class C2C_dealer_create(unittest.TestCase):
    '''
    法币-商家发布挂单，确保商家余额足够
    '''

    def setUp(self):
        obj_token = headertoken.PackgingToken(url_login, token_user,
                                              data_c2c_dealer_create.t_headers_login,
                                              data_c2c_dealer_create.token_clienttype)
        self.token_value = obj_token.gettokenvalue()

    def tearDown(self):
        pass


    def test_No1030101_create_BTC_Sell(self):
        """UCEX QA：dealer creats order_: sell BTC"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_dealer_create.ucex_inputdata[0]
        conf_output_data = data_c2c_dealer_create.ucex_outputdata[0]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_dealer_create.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_dealer_create.t_headers_logged

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

    def test_No1030102_create_ETH_Sell(self):
        """UCEX QA：dealer creats order_: sell ETH"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_dealer_create.ucex_inputdata[1]
        conf_output_data = data_c2c_dealer_create.ucex_outputdata[1]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_dealer_create.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_dealer_create.t_headers_logged

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

    @unittest.skip("I don't want to run this case.")
    def test_No1030103_create_USDT_Sell(self):
        """UCEX QA：dealer creats order_: sell USDT"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_dealer_create.ucex_inputdata[2]
        conf_output_data = data_c2c_dealer_create.ucex_outputdata[2]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_dealer_create.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_dealer_create.t_headers_logged

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


    def test_No1030104_create_BG_Sell(self):
        """UCEX QA：dealer creats order_: sell BG"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_dealer_create.ucex_inputdata[3]
        conf_output_data = data_c2c_dealer_create.ucex_outputdata[3]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_dealer_create.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_dealer_create.t_headers_logged

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

    def test_No1030105_create_Sell_coincode_error(self):
        """UCEX QA：dealer creats order_: sell, but coin code does not exist"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_dealer_create.ucex_inputdata[4]
        conf_output_data = data_c2c_dealer_create.ucex_outputdata[4]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_dealer_create.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_dealer_create.t_headers_logged

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

    def test_No1030106_create_Sell_assetpassword_error(self):
        """UCEX QA：dealer creats order_: sell BTC, but asset password error"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_dealer_create.ucex_inputdata[5]
        conf_output_data = data_c2c_dealer_create.ucex_outputdata[5]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_dealer_create.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_dealer_create.t_headers_logged

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

    def test_No1030107_create_Buy_BTC(self):
        """UCEX QA：dealer creats order_: buy BTC"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_dealer_create.ucex_inputdata[6]
        conf_output_data = data_c2c_dealer_create.ucex_outputdata[6]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_dealer_create.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_dealer_create.t_headers_logged

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

    def test_No1030108_create_Buy_ETH(self):
        """UCEX QA：dealer creats order_: buy ETH"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_dealer_create.ucex_inputdata[7]
        conf_output_data = data_c2c_dealer_create.ucex_outputdata[7]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_dealer_create.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_dealer_create.t_headers_logged

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

    @unittest.skip("I don't want to run this case.")
    def test_No1030109_create_Buy_USDT(self):
        """UCEX QA：dealer creats order_: buy USDT"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_dealer_create.ucex_inputdata[8]
        conf_output_data = data_c2c_dealer_create.ucex_outputdata[8]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_dealer_create.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_dealer_create.t_headers_logged

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


    def test_No1030110_create_Buy_BG(self):
        """UCEX QA：dealer creats order_: buy BG"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_dealer_create.ucex_inputdata[9]
        conf_output_data = data_c2c_dealer_create.ucex_outputdata[9]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_dealer_create.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_dealer_create.t_headers_logged

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

    def test_No1030111_create_Buy_coincode_error(self):
        """UCEX QA：dealer creats order_: buy, but coin code does not exist"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_dealer_create.ucex_inputdata[10]
        conf_output_data = data_c2c_dealer_create.ucex_outputdata[10]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_dealer_create.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_dealer_create.t_headers_logged

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

    def test_No1030112_create_OTC_type_error(self):
        """UCEX QA：dealer creats order_: otc type error"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_dealer_create.ucex_inputdata[11]
        conf_output_data = data_c2c_dealer_create.ucex_outputdata[11]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_dealer_create.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_dealer_create.t_headers_logged

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
