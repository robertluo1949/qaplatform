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
from qaplatform.testdatas.homepage_102 import data_hotcoin_list

##读取配置文件的接口request url  和   request headers
url = data_hotcoin_list.url_hotcoin_list
t_headers = data_hotcoin_list.t_headers






class Homepage_hotcoins_list(unittest.TestCase):
    '''
    热门币列表
    '''

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_No1020501_get_hotcoins_list_succeed(self):
        """UCEX QA：获取热门币列表"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_hotcoin_list.ucex_inputdata[0]
        conf_output_data = data_hotcoin_list.ucex_outputdata[0]

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

