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
url_c2c_trend = config.ENV_DOMAINNAME+"exchange/otc/trades/recently/trend"

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
        "urlparameter":"?currency=CNY&coinCode=101&limit=100",
        "body": { }
    },
    1: {
        "urlparameter": "?currency=CNY&coinCode=104&limit=100",
        "body": {}
    },
    2: {
        "urlparameter": "?currency=CNY&coinCode=106&limit=100",
        "body": {}
    },
    3: {
        "urlparameter": "?currency=CNY&coinCode=208&limit=100",
        "body": {}
    },
    4: {
        "urlparameter": "?currency=CNY&coinCode=999&limit=100",
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
