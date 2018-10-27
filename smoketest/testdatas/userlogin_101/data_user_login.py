# coding:utf-8
"""
title: 自动化测试 UCEX 测试请求和响应数据
author:Robert
date:20180504
email:shuibo.luo@ucextech.com
content:  java user-userlogin_101
other:
"""

import config
##url_login 登录接口
url_login = config.ENV_DOMAINNAME+"exchange/users/api/login"
url_captcha = config.ENV_DOMAINNAME+"exchange/codes/captcha"
url_phonecode = config.ENV_DOMAINNAME+"exchange/codes/phone"

##post header
t_headers = {'Content-Type': 'application/json','request-client-type':'web'}


#login
ucex_userlogin_inputdata ={
    0:{
        "urlparameter":"",
        "body": { "email": "13010001095",  "password": "1qaz@WSX"}
    },
    1: {
        "urlparameter": "",
        "body": {"email": "19999999999", "password": "1qaz@WSX"}},
    2: {
        "urlparameter": "",
        "body": {"email": "13010001095", "password": "error123"}},
    3: {
        "urlparameter": "",
        "body": {"email": "", "password": ""}}
}
ucex_userlogin_outputdata={
    0:{"httpcode":200, "code":200, "result": "Success"},
    1:{"httpcode":401, "code": 1407, "msg": "user not exists"},
    2:{"httpcode":401, "code": 1421, "msg": "Password error, 4 times before locked"},
    3:{"httpcode":400, "code":1408,  "msg": "username is empty"}
}

#captcha
ucex_captcha_inputdata ={
    0: {
        "urlparameter": "",
        "body": {}
    }
}
ucex_captcha_outputdata={0:{"httpcode":200}}


#phonecode
ucex_phonecode_inputdata ={
    0: {
        "urlparameter": "?cpatcha=1234",
        "body": {}
    }
}
ucex_phonecode_outputdata={
    0:{"httpcode":500, "code":99506}
}
