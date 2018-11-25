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
url_phonecode = config.ENV_DOMAINNAME+"exchange/codes/phone"


##post header
t_headers = {'Content-Type': 'application/json','request-client-type':'web'}


ucex_inputdata ={
    0: {
        "urlparameter": "?cpatcha=1234",
        "body": {}
    }
}
ucex_outputdata={
    0:{"httpcode":500, "code":99506}
}
