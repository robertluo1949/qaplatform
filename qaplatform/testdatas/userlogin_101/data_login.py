# coding:utf-8
"""
title: 自动化测试 UCEX 测试请求和响应数据
author:Robert
date:20180504
email:robert_luo1949@163.com
content:  java user-userlogin_101
other:
"""

import config
##urls
url_login = config.ENV_DOMAINNAME+"exchange/users/api/login"



##post header
t_headers = {'Content-Type': 'application/json','request-client-type':'web'}



ucex_inputdata ={
    0:{
        "urlparameter":"",
        "body": { "email": "15298868982",  "password": "test1212"}
    },
    1: {
        "urlparameter": "",
        "body": {"email": "19999999999", "password": "test1212"}},
    2: {
        "urlparameter": "",
        "body": {"email": "15298868982", "password": "error123"}},
    3: {
        "urlparameter": "",
        "body": {"email": "", "password": ""}}
}
ucex_outputdata={
    0:{"httpcode":200, "code":200, "result": "Success"},
    1:{"httpcode":401, "code": 1421, "msg": "Password error, 4 times before locked"},
    2:{"httpcode":401, "code": 1421, "msg": "Password error, 4 times before locked"},
    3:{"httpcode":400, "code":1408,  "msg": "username is empty"}
}
