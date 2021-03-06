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
url_c2c_user_create_trade = config.ENV_DOMAINNAME+"exchange/otc/trades/create"
url_c2c_user_cancle_trade = config.ENV_DOMAINNAME+"exchange/otc/trades/cancel/" #这里最后的斜杠是需要的


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

#一键匹配
ucex_inputdata_buy = {
    "urlparameter": "",
    "body": {"coinCode": "101", "currency": "CNY", "orderQty": "0.05", "totalAmount": "2250.04", "price": "45000.83"}
}

#实际下单
ucex_inputdata_create ={
    "urlparameter": "",
    "body": {"fillQty": "0.0027"}
}

#取消交易
ucex_inputdata ={
    0: {
        "body": {}
    },
    1: {
        "urlparameter": "99999999-9999999-9999999",
        "body": {}
    }
}

ucex_outputdata={
    0: {"httpcode": 200, "code": 200},
    1: {"httpcode": 400, "code": 5700}
}
