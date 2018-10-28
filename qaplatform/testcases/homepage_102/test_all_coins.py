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

from qaplatform.controller.log import logger
from qaplatform.testdatas.homepage_102 import data_allcoins

##读取配置文件的接口request url  和   request headers
url = data_allcoins.url_all_coins
t_headers = data_allcoins.t_headers






class Homepage_all_coins(unittest.TestCase):
    '''
    所有上架币种
    '''

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_No1020401_get_all_coins_succeed(self):
        """UCEX QA：获取当前支持的所有币种列表"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_allcoins.ucex_inputdata[0]
        conf_output_data = data_allcoins.ucex_outputdata[0]

        try:
            response_content = requests.get(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_headers)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_content))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        self.assertIsNotNone(response_output_data['data'], 'data list is none')
        logger.logger.info(self.id())

