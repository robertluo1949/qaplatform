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
from qaplatform.testdatas.homepage_102 import data_user_profile




##读取配置文件的接口request url  和   request headers
url_login = data_user_profile.url_login
token_user = data_user_profile.token_user
t_headers_login = data_user_profile.t_headers_login
t_headers_logged = data_user_profile.t_headers_logged
token_clienttype = data_user_profile.token_clienttype

url = data_user_profile.url_user_profile


class Homepage_user_profile(unittest.TestCase):
    '''
    用户的profile
    '''

    def setUp(self):
        obj_token = headertoken.PackgingToken(url_login, data_user_profile.token_user, data_user_profile.t_headers_login, data_user_profile.token_clienttype)
        self.token_value = obj_token.gettokenvalue()

    def tearDown(self):
        pass


    def test_No1020901_get_user_profile_succeed(self):
        """UCEX QA：获取用户的profile信息"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_user_profile.ucex_inputdata[0]
        conf_output_data = data_user_profile.ucex_outputdata[0]
        logger.logger.info("token value "+str(self.token_value))

        data_user_profile.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_user_profile.t_headers_logged

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
        self.assertIsNotNone(response_output_data['data']['phone'],'returned phone number is none')

        logger.logger.info(self.id())

