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
url_c2c_user_buy = config.ENV_DOMAINNAME+"exchange/otc/orders/easy/buy"

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
        "urlparameter":"",
        "body": {"coinCode": "101", "currency": "CNY", "orderQty": "0.0001", "totalAmount": "4.5", "price": "45000.83"}
    },
    1: {
        "urlparameter": "",
        "body": {"coinCode": "101", "currency": "CNY", "orderQty": "10.0001", "totalAmount": "450012.800", "price": "45000.83"}
    },
    2: {
        "urlparameter": "",
        "body": {"coinCode": "101", "currency": "CNY", "orderQty": "0.02", "totalAmount": "900.01", "price": "5.83"}
    },
    3: {
        "urlparameter": "",
        "body": {"coinCode": "101", "currency": "CNY", "orderQty": "0.02", "totalAmount": "900.01", "price": "45000.83"}
    },
    4: {
        "urlparameter": "",
        "body": {"coinCode": "999", "currency": "CNY", "orderQty": "0.02", "totalAmount": "900.01", "price": "45000.83"}
    },

}
ucex_outputdata={
    0:{"httpcode":400, "code":5208},
    1:{"httpcode": 400, "code": 5208},
    2:{"httpcode": 400, "code": 5891},
    3: {"httpcode": 200, "code": 200},
    4: {"httpcode": 400, "code": 5891}
}
