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
url_captcha = config.ENV_DOMAINNAME+"exchange/codes/captcha"


##post header
t_headers = {'Content-Type': 'application/json','request-client-type':'web'}



ucex_inputdata ={
    0: {
        "urlparameter": "",
        "body": {}
    }
}
ucex_outputdata={
    0:{"httpcode":200}
}
