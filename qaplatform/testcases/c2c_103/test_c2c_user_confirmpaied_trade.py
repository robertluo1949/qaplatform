# coding:utf-8
'''
title: 自动化测试 UCEX
author: bessie
date: 20180917
email:
content: 为了实时获取可以取消的交易id, 先去做一键匹配，去下单，然后再去确认付款这笔单子
        所以测试过程中不需要依赖什么数据
other:
'''
import json
import unittest

import requests

from qaplatform.controller.libs.ucexbackend import headertoken
from qaplatform.controller.log import logger
from qaplatform.testdatas.c2c_103 import data_c2c_user_confirmpaied_trade



##读取配置文件的接口request url  和   request headers
url_login = data_c2c_user_confirmpaied_trade.url_login
token_user = data_c2c_user_confirmpaied_trade.token_user
t_headers_login = data_c2c_user_confirmpaied_trade.t_headers_login
t_headers_logged = data_c2c_user_confirmpaied_trade.t_headers_logged
token_clienttype = data_c2c_user_confirmpaied_trade.token_clienttype

url_buy = data_c2c_user_confirmpaied_trade.url_c2c_user_buy
url_create = data_c2c_user_confirmpaied_trade.url_c2c_user_create_trade
url = data_c2c_user_confirmpaied_trade.url_c2c_user_confirmpaied_trade


class C2C_confirm_trade(unittest.TestCase):
    '''
    法币购买-下买单,然后确认已付款
    '''

    def setUp(self):
        obj_token = headertoken.PackgingToken(url_login, token_user,
                                              data_c2c_user_confirmpaied_trade.t_headers_login,
                                              data_c2c_user_confirmpaied_trade.token_clienttype)
        self.token_value = obj_token.gettokenvalue()

    def tearDown(self):
        pass

    # @unittest.skip("I don't want to run this case.")
    def test_No1031201_buy_BTC_confirm_trade_success(self):
        """UCEX QA：buy BTC, get the order id and create trade, then confirm paied"""
        logger.logger.debug("doing test " + str(self.id()) + " started")
        # 一键匹配需要的数据
        conf_input_data_buy = data_c2c_user_confirmpaied_trade.ucex_inputdata_buy

        # 下单需要的数据
        conf_input_data_create = data_c2c_user_confirmpaied_trade.ucex_inputdata_create

        #确认已付款需要的数据
        conf_input_data = data_c2c_user_confirmpaied_trade.ucex_inputdata[0]
        conf_output_data = data_c2c_user_confirmpaied_trade.ucex_outputdata[0]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_user_confirmpaied_trade.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_user_confirmpaied_trade.t_headers_logged

        # get the current available otc orders
        try:
            response_content_buy = requests.post(str(url_buy + conf_input_data_buy["urlparameter"]),
                                                 data=json.dumps(conf_input_data_buy["body"]), headers=t_header)
            response_output_data_buy = response_content_buy.json()
        except BaseException as be:
            logger.logger.exception("baseException  " + str(be))
        except Exception as e:
            logger.logger.exception("Exception " + str(e))
        otc_order_id = response_output_data_buy["data"]["id"]
        dealer_payment_id = response_output_data_buy["data"]["payments"][0]["id"]
        logger.logger.info(otc_order_id)
        logger.logger.info(dealer_payment_id)

        # create trade
        try:
            conf_input_data_create["body"]["otcOrderId"] = otc_order_id
            conf_input_data_create["body"]["userPaymentId"] = dealer_payment_id
            response_content_create = requests.post(str(url_create + conf_input_data_create["urlparameter"]),
                                             data=json.dumps(conf_input_data_create["body"]),
                                             headers=t_header)
            response_output_data_create = response_content_create.json()
            logger.logger.info(response_output_data_create['data']['otcTradeNo'])
        except BaseException as be:
            logger.logger.exception("baseException  " + str(be))
        except Exception as e:
            logger.logger.exception("Exception " + str(e))


        # confirm trade
        try:
            otc_trade_id = response_output_data_create['data']['otcTradeNo']
            conf_input_data["urlparameter"] = otc_trade_id
            response_content = requests.get(str(url + conf_input_data["urlparameter"]),data=json.dumps(conf_input_data["body"]),headers=t_header)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  " + str(be))
        except Exception as e:
            logger.logger.exception("Exception " + str(e))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')

        logger.logger.info(self.id())


    @unittest.skip("I don't want to run this case.")
    def test_No1031202_cancle_unexist_trade(self):
        """UCEX QA： cancle otc buy trade, but trade id not exist"""
        logger.logger.debug("doing test " + str(self.id()) + " started")

        #取消交易需要的数据
        conf_input_data = data_c2c_user_confirmpaied_trade.ucex_inputdata[1]
        conf_output_data = data_c2c_user_confirmpaied_trade.ucex_outputdata[1]
        logger.logger.info("token value "+str(self.token_value))

        data_c2c_user_confirmpaied_trade.t_headers_logged["ucex-web-api-token"] = self.token_value
        t_header = data_c2c_user_confirmpaied_trade.t_headers_logged

        # cancle trade
        try:
            response_content = requests.get(str(url + conf_input_data["urlparameter"]),
                                             data=json.dumps(conf_input_data["body"]),
                                             headers=t_header)
            response_output_data = response_content.json()
        except BaseException as be:
            logger.logger.exception("baseException  " + str(be))
        except Exception as e:
            logger.logger.exception("Exception " + str(e))

        self.assertEqual(response_content.status_code, conf_output_data['httpcode'], 'httpcode is not correct ')
        self.assertEqual(response_output_data['code'], conf_output_data['code'],    'requests status code  error')

        logger.logger.info(self.id())



