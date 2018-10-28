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
url_c2c_recently = config.ENV_DOMAINNAME+"exchange/otc/trades/recently"

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
        "urlparameter":"?otcTradeStatus=FINISHED&coinCode=101&currency=CNY&offset=0&limit=10",
        "body": { }
    },
    1: {
        "urlparameter":"?otcTradeStatus=FINISHED&coinCode=104&currency=CNY&offset=0&limit=10",
        "body": {}
    },
    2: {
        "urlparameter":"?otcTradeStatus=FINISHED&coinCode=106&currency=CNY&offset=0&limit=10",
        "body": {}
    },
    3: {
        "urlparameter":"?otcTradeStatus=FINISHED&coinCode=208&currency=CNY&offset=0&limit=10",
        "body": {}
    },
    4: {
        "urlparameter":"?otcTradeStatus=FINISHED&coinCode=999&currency=CNY&offset=0&limit=10",
        "body": {}
    }

}
ucex_outputdata={
    0:{"httpcode":200, "code":200},
    1: {"httpcode": 200, "code": 200},
    2: {"httpcode": 200, "code": 200},
    3: {"httpcode": 200, "code": 200},
    4: {"httpcode": 200, "code": 200}
}
