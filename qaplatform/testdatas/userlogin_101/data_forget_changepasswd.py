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
##urls
url_forget_changepass = config.ENV_DOMAINNAME+"exchange/users/forgot/change/password"


##post header
t_headers = {'Content-Type': 'application/json','request-client-type':'web'}



ucex_inputdata ={
    0: {
        "urlparameter": "?code=1234",
        "body": {"communicationMethod": "15298868981",
                 "password":"test1212"}
    }
}
ucex_outputdata={
    0:{"httpcode":400,
       "code":1430
       }
}
