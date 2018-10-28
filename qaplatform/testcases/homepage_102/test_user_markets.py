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
from qaplatform.testdatas.homepage_102 import data_user_markets




##读取配置文件的接口request url  和   request headers
url_login = data_user_markets.url_login
token_user = data_user_markets.token_user
t_headers_login = data_user_markets.t_headers_login
t_headers_logged = data_user_markets.t_headers_logged
token_clienttype = data_user_markets.token_clienttype

url = data_user_markets.url_user_markets


class Homepage_user_markets(unittest.TestCase):
    '''
    用户的自选市场列表
    '''

    def setUp(self):
        obj_token = headertoken.PackgingToken(url_login, data_user_markets.token_user, data_user_markets.t_headers_login, data_user_markets.token_clienttype)
        self.token_value = obj_token.gettokenvalue()

    def tearDown(self):
        pass


    def test_No1020801_get_user_markets_succeed(self):
        """UCEX QA：获取当前用户自选的市场列表"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_user_markets.ucex_inputdata[0]
        conf_output_data = data_user_markets.ucex_outputdata[0]
        logger.logger.info("token value "+str(self.token_value))

        data_user_markets.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_user_markets.t_headers_logged

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

