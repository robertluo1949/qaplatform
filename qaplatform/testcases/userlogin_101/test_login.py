# coding:utf-8
'''
title: 自动化测试 UCEX
author:Robert
date:20180504
email:shuibo.luo@ucextech.com
content:  java user-userlogin_101
other:
'''
import json
import unittest

import requests

from qaplatform.controller.log import logger
from qaplatform.testdatas.userlogin_101 import data_login

##读取配置文件的接口request url  和   request headers
url = data_login.url_login
t_headers = data_login.t_headers




class User_login(unittest.TestCase):
    '''
    login模块的测试
    '''

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_No1010101_login_succeed(self):
        """UCEX QA：验证web用户能用手机号登录成功"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_login.ucex_inputdata[0]
        conf_output_data = data_login.ucex_outputdata[0]


        try:
            response_content = requests.post(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_headers)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],' requests status code  error')
        self.assertEqual(response_output_data['result'], conf_output_data['result'],' requests status  error')
        logger.logger.info(self.id())

    def test_No1010102_login_nonexistphone(self):
        """UCEX QA：验证手机号不存在，登陆失败"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_login.ucex_inputdata[1]
        conf_output_data = data_login.ucex_outputdata[1]


        try:
            response_content = requests.post(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_headers)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        logger.logger.info(self.id())



    def test_No1010103_login_errorpasswd(self):
        """UCEX QA：验证密码错误，登陆失败"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_login.ucex_inputdata[2]
        conf_output_data = data_login.ucex_outputdata[2]


        try:
            response_content = requests.post(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_headers)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        self.assertEqual(response_output_data['msg'], conf_output_data['msg'], 'requests status  error')
        logger.logger.info(self.id())


    def test_No1010104_login_emptyparameters(self):
        """UCEX QA：验证参数为空，登陆失败"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_login.ucex_inputdata[3]
        conf_output_data = data_login.ucex_outputdata[3]


        try:
            response_content = requests.post(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_headers)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        self.assertEqual(response_output_data['msg'], conf_output_data['msg'], 'requests status  error')
        logger.logger.info(self.id())