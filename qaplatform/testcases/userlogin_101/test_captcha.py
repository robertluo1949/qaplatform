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

from qaplatform.controller.log import logger
from qaplatform.testdatas.userlogin_101 import data_captcha

##读取配置文件的接口request url  和   request headers
url = data_captcha.url_captcha
t_headers = data_captcha.t_headers






class User_captcha(unittest.TestCase):
    '''
    captcha 图形验证码的测试
    '''

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_No1010201_getcapatcha_succeed(self):
        """UCEX QA：验证web用户获取图像验证码成功"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_captcha.ucex_inputdata[0]
        conf_output_data = data_captcha.ucex_outputdata[0]

        try:
            response_content = requests.get(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_headers)
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        logger.logger.info(self.id())

