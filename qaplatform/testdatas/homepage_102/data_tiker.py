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
url_tikcer_24h= config.ENV_DOMAINNAME+"exchange/coins/tick/24h"



##post header
t_headers = {'Content-Type': 'application/json','request-client-type':'web'}



ucex_inputdata ={
	0:{
		"urlparameter":"?coinCode=&history=false",
		"body": { }
	},
	1: {
		"urlparameter": "?coinCode=&history=true",
		"body": {}
	},
	2: {
		"urlparameter": "?coinCode=101,106,102,103,104&history=true",
		"body": {}
	}

}
ucex_outputdata={
	0:{"httpcode":200, "code":200, "result": "Success"},
	1:{"httpcode":200, "code":200, "result": "Success"},
	2:{"httpcode":200, "code":200, "result": "Success"}
}
