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

from smoketest.controller.log import logger
from smoketest.testdatas.homepage_102 import data_tiker

##读取配置文件的接口request url  和   request headers
url = data_tiker.url_tikcer_24h
t_headers = data_tiker.t_headers




class tiker_24h(unittest.TestCase):
    '''
    java tikcer_24
    '''

    def setUp(self):
        pass

    def tearDown(self):
        pass


    def test_No1020701_coinstiker_history_false(self):
        """UCEX QA：ticker 不需要历史数据"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_tiker.ucex_inputdata[0]
        conf_output_data = data_tiker.ucex_outputdata[0]


        try:
            response_content = requests.get(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_headers)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        self.assertListEqual(response_output_data['data'][0]['history'],[], 'history list is not empty')
        logger.logger.info(self.id())


    def test_No1020702_coinstiker_history_true_and_allcoins(self):
        """UCEX QA：ticker 不指定币种，获取所有币种，而且需要历史数据"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_tiker.ucex_inputdata[1]
        conf_output_data = data_tiker.ucex_outputdata[1]


        try:
            response_content = requests.get(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_headers)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        self.assertIsNotNone(response_output_data['data'][0]['history'], 'history list is none')
        logger.logger.info(self.id())


    def test_No1020703_coinstiker_history_true_and_specify_coins(self):
        """UCEX QA：ticker 指定币种，而且需要历史数据"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        conf_input_data = data_tiker.ucex_inputdata[2]
        conf_output_data = data_tiker.ucex_outputdata[2]


        try:
            response_content = requests.get(str(url+conf_input_data["urlparameter"]), data=json.dumps(conf_input_data["body"]), headers=t_headers)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  "+str(be))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        logger.logger.info(str(response_output_data))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')
        self.assertIsNotNone(response_output_data['data'][0]['history'], 'history list is none')
        logger.logger.info(self.id())


