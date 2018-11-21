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
url_c2c_remind = config.ENV_DOMAINNAME+"exchange/otc/trade/remind"

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
        "urlparameter":"?time=",
        "body": { }
    }


}
ucex_outputdata={
    0:{"httpcode":200, "code":200}
}
