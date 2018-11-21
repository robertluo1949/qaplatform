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
url_c2c_listed = config.ENV_DOMAINNAME+"exchange/otc/orders/current/listed"

##post_requests header
t_headers_login = {'Content-Type': 'application/json', 'request-client-type': 'web'}
t_headers_logged ={'Content-Type': 'application/json', 'ucex-web-api-token': None}

##post_requests token_type
token_clienttype = "ucex-web-api-token"
token_user = {
  "email":"+8615298868982",
  "password":"test1212",
  "username":"+8615298868982"
}



ucex_inputdata ={
    0:{
        "urlparameter":"?otcOrderStatus=NEW,PARTIALLY_FILLED&otcOrderType=SELL&offset=0&limit=10&orderStr=price+asc&currency=CNY&coinCode=101",
        "body": { }
    },
    1: {
        "urlparameter":"?otcOrderStatus=NEW,PARTIALLY_FILLED&otcOrderType=SELL&offset=0&limit=10&orderStr=price+asc&currency=CNY&coinCode=104",
        "body": {}
    },
    2: {
        "urlparameter":"?otcOrderStatus=NEW,PARTIALLY_FILLED&otcOrderType=SELL&offset=0&limit=10&orderStr=price+asc&currency=CNY&coinCode=106",
        "body": {}
    },
    3: {
        "urlparameter":"?otcOrderStatus=NEW,PARTIALLY_FILLED&otcOrderType=SELL&offset=0&limit=10&orderStr=price+asc&currency=CNY&coinCode=208",
        "body": {}
    },
    4: {
        "urlparameter": "?otcOrderStatus=NEW,PARTIALLY_FILLED&otcOrderType=BUY&offset=0&limit=10&orderStr=price+asc&currency=CNY&coinCode=999",
        "body": {}
    },
    5: {
        "urlparameter": "?otcOrderStatus=NEW,PARTIALLY_FILLED&otcOrderType=BUY&offset=0&limit=10&orderStr=price+asc&currency=CNY&coinCode=101",
        "body": {}
    },
    6: {
        "urlparameter": "?otcOrderStatus=NEW,PARTIALLY_FILLED&otcOrderType=BUY&offset=0&limit=10&orderStr=price+asc&currency=CNY&coinCode=104",
        "body": {}
    },
    7: {
        "urlparameter": "?otcOrderStatus=NEW,PARTIALLY_FILLED&otcOrderType=BUY&offset=0&limit=10&orderStr=price+asc&currency=CNY&coinCode=106",
        "body": {}
    },
    8: {
        "urlparameter": "?otcOrderStatus=NEW,PARTIALLY_FILLED&otcOrderType=BUY&offset=0&limit=10&orderStr=price+asc&currency=CNY&coinCode=208",
        "body": {}
    },
    9: {
        "urlparameter": "?otcOrderStatus=NEW,PARTIALLY_FILLED&otcOrderType=BOTH&offset=0&limit=10&orderStr=price+asc&currency=CNY&coinCode=208",
        "body": {}
    }

}
ucex_outputdata={
    0:{"httpcode":200, "code":200},
    1: {"httpcode": 200, "code": 200},
    2: {"httpcode": 200, "code": 200},
    3: {"httpcode": 200, "code": 200},
    4: {"httpcode": 200, "code": 200},
    5: {"httpcode": 200, "code": 200},
    6: {"httpcode": 200, "code": 200},
    7: {"httpcode": 200, "code": 200},
    8: {"httpcode": 200, "code": 200},
    9: {"httpcode": 500, "code": 99506}

}
