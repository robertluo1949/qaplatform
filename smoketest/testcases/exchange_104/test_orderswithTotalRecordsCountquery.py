# coding:utf-8
'''
title: 自动化测试 UCEX
author:Robert
date:20180504
email:shuibo.luo@ucextech.com
content:  orderswithTotalRecordsCountquery
other:
'''


import json
import unittest

import requests

from smoketest.controller.libs.ucexbackend import headertoken
from smoketest.controller.log import logger
from smoketest.testdatas.exchange_104 import data_orderswithTotalRecordsCountquery

##读取配置文件的接口request url  和   request headers
url_login = data_orderswithTotalRecordsCountquery.url_login
token_user = data_orderswithTotalRecordsCountquery.token_user
url = data_orderswithTotalRecordsCountquery.url_withTotalRecordsCountquery
t_headers_login = data_orderswithTotalRecordsCountquery.t_headers_login
t_header_order =  data_orderswithTotalRecordsCountquery.t_headers_order
token_clienttype = data_orderswithTotalRecordsCountquery.token_clienttype


class withTotalRecordsCount(unittest.TestCase):
    '''
    java ucex exchange 模块的测试
    '''
    # def __init__(self):
    #     token_value =self.token_value
    #     print("token")
    def setUp(self):

        obj_token =headertoken.PackgingToken(url_login, data_orderswithTotalRecordsCountquery.token_user, data_orderswithTotalRecordsCountquery.t_headers_login, token_clienttype)
        self.token_value =obj_token.gettokenvalue()

    def tearDown(self):
        pass


    def test_No1040301_historyquery(self):
        """UCEX QA：验证币币交易, 历史委托查询成功"""
        logger.logger.debug("doding test " + str(self.id()) + " started")
        logger.logger.info("token value "+str(self.token_value))

        data_orderswithTotalRecordsCountquery.t_headers_order["ucex-web-api-token"] =self.token_value
        t_header = data_orderswithTotalRecordsCountquery.t_headers_order
        conf_input_data = data_orderswithTotalRecordsCountquery.ucex_withTotalRecordsCountquery_inputdata[1]
        conf_output_data = data_orderswithTotalRecordsCountquery.ucex_withTotalRecordsCountquery_outputdata[1]


        try:
            response_content = requests.get(url, data=json.dumps(conf_input_data["body"]), headers=t_header)
            response_output_data = response_content.json()
            logger.logger.info("response_output_data  "+str(response_output_data))

        except BaseException as be:
            logger.logger.exception("baseExcetpion  "+str(be)+"  "+str(response_output_data))
        except Exception as e:
            logger.logger.exception("Excetpion "+str(e)+"  "+str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'respones status code  error')
        self.assertNotEqual(response_output_data['data']["orders"], conf_output_data['data']["orders"],    'respones data orders  error')




