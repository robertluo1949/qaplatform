# coding:utf-8
'''
title: 自动化测试 UCEX
author:Robert
date:20180504
email:shuibo.luo@ucextech.com
content:  java user-phonecode_101
other:
'''
import json
import unittest

import requests

from smoketest.controller.log import logger
from smoketest.testdatas.userlogin_101 import data_register

##读取配置文件的接口request url  和   request headers
url = data_register.url_register
t_headers = data_register.t_headers






class User_register(unittest.TestCase):
    '''
    注册
    '''

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_No1010801_register_failed(self):
        """UCEX QA：图形验证码和短信验证码都输入错误，注册失败"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_register.ucex_inputdata[0]
        conf_output_data = data_register.ucex_outputdata[0]

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

