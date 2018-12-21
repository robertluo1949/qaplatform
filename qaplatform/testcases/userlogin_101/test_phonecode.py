# coding:utf-8
'''
title: 自动化测试 UCEX
author:Robert
date:20180504
email:robert_luo1949@163.com
content:  java user-phonecode_101
other:
'''
import json
import unittest

import requests

from qaplatform.controller.log import logger
from qaplatform.testdatas.userlogin_101 import data_phonecode

##读取配置文件的接口request url  和   request headers
url = data_phonecode.url_phonecode
t_headers = data_phonecode.t_headers






class User_phonecode(unittest.TestCase):
    '''
    phonecode  获取短信验证码，只验证码图像验证码错误的情况
    '''

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_No1010301_errorcode(self):
        """UCEX QA：验证web获取短信验证码，图像验证码输入错误"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_phonecode.ucex_inputdata[0]
        conf_output_data = data_phonecode.ucex_outputdata[0]

        try:
            response_content = requests.post(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_headers)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        logger.logger.info(self.id())

