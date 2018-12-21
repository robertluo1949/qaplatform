# coding:utf-8
'''
title: 自动化测试 UCEX
author:Robert
date:20180504
email:robert_luo1949@163.com
content:
other:
'''
import json
import unittest

import requests

from qaplatform.controller.log import logger
from qaplatform.testdatas.userlogin_101 import data_forget_changepasswd

##读取配置文件的接口request url  和   request headers
url = data_forget_changepasswd.url_forget_changepass
t_headers = data_forget_changepasswd.t_headers






class User_forget_changepasswd(unittest.TestCase):
    """
    找回密码
   """

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_No1010701_forget_changepasswd(self):
        "UCEX QA：验证web用户忘记密码, 但是验证码错误，无法重置密码"
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_forget_changepasswd.ucex_inputdata[0]
        conf_output_data = data_forget_changepasswd.ucex_outputdata[0]

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

