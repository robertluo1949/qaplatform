# coding:utf-8
"""
title: 自动化测试 UCEX 测试请求和响应数据
author: bessie
date: 20180917
email:
content:
other:
"""

import config
##urls
url_login = config.ENV_DOMAINNAME+"exchange/users/api/login"
url_c2c_dealer_create = config.ENV_DOMAINNAME+"exchange/otc/orders/create"

##post_requests header
t_headers_login = {'Content-Type': 'application/json', 'request-client-type': 'web'}
t_headers_logged ={'Content-Type': 'application/json', 'ucex-web-api-token': None}

##post_requests token_type
token_clienttype = "ucex-web-api-token"
dealer_token_user = {
  "email":"+8613010001097",
  "password":"1qaz@WSX",
  "username":"+8613010001097"
}


ucex_inputdata ={
    0:{
        "urlparameter":"",
        "body": {"assetPassword":"123456","coinCode":101,"currency":"CNY","orderQty":"100",
                 "otcOrderType":"SELL","price":"45000","remark":"","minLimitMoney":"","maxLimitMoney":""}
    },
    1: {
        "urlparameter": "",
        "body": {"assetPassword": "123456", "coinCode": 104, "currency": "CNY", "orderQty": "100",
                 "otcOrderType": "SELL", "price": "1958.12", "remark": "", "minLimitMoney": "", "maxLimitMoney": ""}
    },
    2: {
        "urlparameter": "",
        "body": {"assetPassword": "123456", "coinCode": 106, "currency": "CNY", "orderQty": "10000",
                 "otcOrderType": "SELL", "price": "6.98", "remark": "", "minLimitMoney": "", "maxLimitMoney": ""}
    },
    3: {
        "urlparameter": "",
        "body": {"assetPassword": "123456", "coinCode": 208, "currency": "CNY", "orderQty": "1000000",
                 "otcOrderType": "SELL", "price": "0.005", "remark": "", "minLimitMoney": "", "maxLimitMoney": ""}
    },
    4: {
        "urlparameter": "",
        "body": {"assetPassword": "123456", "coinCode": 999, "currency": "CNY", "orderQty": "100",
                 "otcOrderType": "SELL", "price": "45000", "remark": "", "minLimitMoney": "", "maxLimitMoney": ""}
    },
    5: {
        "urlparameter": "",
        "body": {"assetPassword": "654321", "coinCode": 101, "currency": "CNY", "orderQty": "100",
                 "otcOrderType": "SELL", "price": "45000", "remark": "", "minLimitMoney": "", "maxLimitMoney": ""}
    },
    6: {
        "urlparameter": "",
        "body": {"assetPassword": "", "coinCode": 101, "currency": "CNY", "orderQty": "100",
                 "otcOrderType": "BUY", "price": "45000", "remark": "", "minLimitMoney": "", "maxLimitMoney": ""}
    },
    7: {
        "urlparameter": "",
        "body": {"assetPassword": "", "coinCode": 104, "currency": "CNY", "orderQty": "100",
                 "otcOrderType": "BUY", "price": "1958.12", "remark": "", "minLimitMoney": "", "maxLimitMoney": ""}
    },
    8: {
        "urlparameter": "",
        "body": {"assetPassword": "", "coinCode": 106, "currency": "CNY", "orderQty": "10000",
                 "otcOrderType": "BUY", "price": "6.98", "remark": "", "minLimitMoney": "", "maxLimitMoney": ""}
    },
    9: {
        "urlparameter": "",
        "body": {"assetPassword": "", "coinCode": 208, "currency": "CNY", "orderQty": "1000000",
                 "otcOrderType": "BUY", "price": "0.005", "remark": "", "minLimitMoney": "", "maxLimitMoney": ""}
    },
    10: {
        "urlparameter": "",
        "body": {"assetPassword": "", "coinCode": 999, "currency": "CNY", "orderQty": "100",
                 "otcOrderType": "BUY", "price": "45000", "remark": "", "minLimitMoney": "", "maxLimitMoney": ""}
    },
    11: {
        "urlparameter": "",
        "body": {"assetPassword": "", "coinCode": 208, "currency": "CNY", "orderQty": "1000000",
                 "otcOrderType": "BOTH", "price": "0.005", "remark": "", "minLimitMoney": "", "maxLimitMoney": ""}
    }

}
ucex_outputdata={
    0:{"httpcode":200, "code":200},
    1: {"httpcode": 200, "code": 200},
    2: {"httpcode": 200, "code": 200},
    3: {"httpcode": 200, "code": 200},
    4: {"httpcode": 500, "code": 99506},
    5: {"httpcode": 400, "code": 1427},
    6: {"httpcode": 200, "code": 200},
    7: {"httpcode": 200, "code": 200},
    8: {"httpcode": 200, "code": 200},
    9: {"httpcode": 200, "code": 200},
    10: {"httpcode": 500, "code": 99506},
    11: {"httpcode": 500, "code": 99506}
}
