# coding:utf-8
'''
title: 自动化测试 UCEX
author:Robert
date:20180504
email:shuibo.luo@ucextech.com
content:
other:
'''
import json
import unittest

import requests

from smoketest.controller.log import logger
from smoketest.testdatas.userlogin_101 import data_forget_effective

##读取配置文件的接口request url  和   request headers
url = data_forget_effective.url_forget_effective
t_headers = data_forget_effective.t_headers






class User_forgeteffective(unittest.TestCase):
    '''
    captcha 图形验证码的测试
    '''

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_No1010501_forgeteffective(self):
        """UCEX QA：验证web用户获取图像验证码成功"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_forget_effective.ucex_inputdata[0]
        conf_output_data = data_forget_effective.ucex_outputdata[0]

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

