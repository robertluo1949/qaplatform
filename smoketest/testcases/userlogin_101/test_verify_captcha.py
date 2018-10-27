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
from smoketest.testdatas.userlogin_101 import data_verify_captcha

##读取配置文件的接口request url  和   request headers
url = data_verify_captcha.url_verify_captcha
t_headers = data_verify_captcha.t_headers






class User_verifycaptcha(unittest.TestCase):
    '''
    验证图形验证码
    '''

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_No1010401_verifycapatcha(self):
        """UCEX QA：验证用户输入的图形验证码"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_verify_captcha.ucex_inputdata[0]
        conf_output_data = data_verify_captcha.ucex_outputdata[0]

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

