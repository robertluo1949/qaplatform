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
url_c2c_get_trade_message = config.ENV_DOMAINNAME+"ucex-controller/msg/getMessages"

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
        "body": {"currentPage": 1, "pageSize": 999, "orderNo": "101e6571-9d8d-4d72-927e-44a8eb97261c"}
    },
    1:{
        "urlparameter":"",
        "body": {"currentPage": 1, "pageSize": 999, "orderNo": "99999999-99999999-999999999-99999999"}
    }
}
ucex_outputdata={
    0:{"httpcode":200, "code":200},
    1: {"httpcode": 200, "code": 200}
}
