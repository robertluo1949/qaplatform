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
from smoketest.testdatas.c2c_103 import  data_c2c_query_orders




##读取配置文件的接口request url  和   request headers
url_login = data_c2c_query_orders.url_login
token_user = data_c2c_query_orders.token_user
t_headers_login = data_c2c_query_orders.t_headers_login
t_headers_logged = data_c2c_query_orders.t_headers_logged
token_clienttype = data_c2c_query_orders.token_clienttype

url = data_c2c_query_orders.url_c2c_query_order


class C2C_queryOrders(unittest.TestCase):
    '''
    法币-我的全部订单
    '''

    def setUp(self):
        obj_token = headertoken.PackgingToken(url_login, data_c2c_query_orders.token_user, data_c2c_query_orders.t_headers_login, data_c2c_query_orders.token_clienttype)
        self.token_value = obj_token.gettokenvalue()

    def tearDown(self):
        pass


    def test_No1030501_query_all_orders(self):
        """UCEX QA：我的全部订单，默认查询全部"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[0]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[0]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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

    def test_No1030502_query_by_otc_client_tradeno(self):
        """UCEX QA：我的全部订单，根据otc_client_trade_no查询"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[1]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[1]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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

    def test_No1030503_query_by_otc_type_sell(self):
        """UCEX QA：我的全部订单，查询卖出类型"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[2]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[2]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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

    def test_No1030504_query_by_otc_type_buy(self):
        """UCEX QA：我的全部订单，查询买的类型"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[3]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[3]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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

    def test_No1030505_query_by_otc_type_error(self):
        """UCEX QA：我的全部订单，查询一个不存在的类型"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[4]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[4]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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

    def test_No1030506_query_by_otc_status_completed(self):
        """UCEX QA：我的全部订单，查询已完成状态的订单"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[5]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[5]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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

    def test_No1030507_query_by_otc_BTC(self):
        """UCEX QA：我的全部订单，查询币种为BTC的订单"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[6]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[6]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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

    def test_No1030508_query_by_otc_ETH(self):
        """UCEX QA：我的全部订单，查询币种为ETH的订单"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[7]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[7]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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

    def test_No1030509_query_by_otc_USDT(self):
        """UCEX QA：我的全部订单，查询币种为USDT的订单"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[8]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[8]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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

    def test_No1030510_query_by_otc_BG(self):
        """UCEX QA：我的全部订单，查询币种为BG的订单"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[9]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[9]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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

    def test_No1030511_query_by_otc_coincode_error(self):
        """UCEX QA：我的全部订单，查询币种不存在"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[10]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[10]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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


    def test_No1030512_query_by_otc_date(self):
        """UCEX QA：我的全部订单，根据起止时间查询"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[11]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[11]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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

    def test_No1030513_query_by_otc_complex(self):
        """UCEX QA：我的全部订单，交易号+类型+时间+币种组合查询"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_query_orders.ucex_inputdata[12]
        conf_output_data = data_c2c_query_orders.ucex_outputdata[12]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_query_orders.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_query_orders.t_headers_logged

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