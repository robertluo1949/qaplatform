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
from smoketest.testdatas.c2c_103 import  data_c2c_remind




##读取配置文件的接口request url  和   request headers
url_login = data_c2c_remind.url_login
token_user = data_c2c_remind.token_user
t_headers_login = data_c2c_remind.t_headers_login
t_headers_logged = data_c2c_remind.t_headers_logged
token_clienttype = data_c2c_remind.token_clienttype

url = data_c2c_remind.url_c2c_remind


class C2C_remind(unittest.TestCase):
    '''
    法币-提醒商家是否有新订单
    '''

    def setUp(self):
        obj_token = headertoken.PackgingToken(url_login, data_c2c_remind.token_user, data_c2c_remind.t_headers_login, data_c2c_remind.token_clienttype)
        self.token_value = obj_token.gettokenvalue()

    def tearDown(self):
        pass


    def test_No1031301_get_remind(self):
        """UCEX QA：dealer transaction remind"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_c2c_remind.ucex_inputdata[0]
        conf_output_data = data_c2c_remind.ucex_outputdata[0]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_remind.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_remind.t_headers_logged

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

