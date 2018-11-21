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
url_c2c_query_order = config.ENV_DOMAINNAME+"exchange/otc/trades/user/query"

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
        "urlparameter":"?otcTradeStatus=&otcTradeId=&coinCode=&otcOrderType=&offset=-10&limit=10",
        "body": { }
    },
    1: {
        "urlparameter":"?otcClientTradeNo=11370872746017792",
        "body": {}
    },
    2: {
        "urlparameter":"?otcTradeStatus=&otcTradeId=&coinCode=&otcOrderType=SELL&offset=-10&limit=10",
        "body": {}
    },
    3: {
        "urlparameter":"?otcTradeStatus=&otcTradeId=&coinCode=&otcOrderType=BUY&offset=-10&limit=10",
        "body": {}
    },
    4: {
        "urlparameter": "?otcTradeStatus=&otcTradeId=&coinCode=&otcOrderType=BOTH&offset=-10&limit=10",
        "body": {}
    },
    5: {
        "urlparameter":"?otcTradeStatus=FINISHED,SELLER_RECEIVED&otcTradeId=&coinCode=&otcOrderType=&offset=-10&limit=10",
        "body": {}
    },
    6: {
        "urlparameter": "?otcTradeStatus=&otcTradeId=&coinCode=101&otcOrderType=&offset=-10&limit=10",
        "body": {}
    },
    7: {
        "urlparameter": "?otcTradeStatus=&otcTradeId=&coinCode=104&otcOrderType=&offset=-10&limit=10",
        "body": {}
    },
    8: {
        "urlparameter": "?otcTradeStatus=&otcTradeId=&coinCode=106&otcOrderType=&offset=-10&limit=10",
        "body": {}
    },
    9: {
        "urlparameter": "?otcTradeStatus=&otcTradeId=&coinCode=208&otcOrderType=&offset=-10&limit=10",
        "body": {}
    },
    10: {
        "urlparameter": "?otcTradeStatus=&otcTradeId=&coinCode=999&otcOrderType=&offset=-10&limit=10",
        "body": {}
    },
    11: {
        "urlparameter": "?otcTradeStatus=&otcTradeId=&coinCode=&otcOrderType=&offset=-10&limit=10&startTime=1535731200000&endTime=1538323199000",
        "body": {}
    },
    12: {
        "urlparameter": "?otcTradeStatus=FINISHED,SELLER_RECEIVED&otcTradeId=&coinCode=106&otcOrderType=SELL&offset=-10&limit=10&startTime=1535731200000&endTime=1538323199000",
        "body": {}
    }

}
ucex_outputdata={
    0:{"httpcode":200, "code":200},
    1: {"httpcode": 200, "code": 200},
    2: {"httpcode": 200, "code": 200},
    3: {"httpcode": 200, "code": 200},
    4: {"httpcode": 500, "code": 99506},
    5: {"httpcode": 200, "code": 200},
    6: {"httpcode": 200, "code": 200},
    7: {"httpcode": 200, "code": 200},
    8: {"httpcode": 200, "code": 200},
    9: {"httpcode": 200, "code": 200},
    10: {"httpcode": 200, "code": 200},
    11: {"httpcode": 200, "code": 200},
    12: {"httpcode": 200, "code": 200}
}
