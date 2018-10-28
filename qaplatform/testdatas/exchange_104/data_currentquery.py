

import config
##url_login 登录接口
url_login = config.ENV_DOMAINNAME+"exchange/users/api/login"
url_withTotalRecordsCountquery =config.ENV_DOMAINNAME+\
                          "exchange/orders/withTotalRecordsCount/current"

##post_requests header
t_headers_login = {'Content-Type': 'application/json', 'request-client-type': 'web'}
t_headers_order ={'Content-Type': 'application/json', 'ucex-web-api-token': None}

##post_requests token_type
token_clienttype = "ucex-web-api-token"
token_user = {
    1: {"email":"+8613010001095","password":"1qaz@WSX","username":"+8613010001095"},
    2: {"email": "+8613010001095", "password": "1qaz@WSX", "username": "+8613010001095"},
    3: {"email": "+8613010001095", "password": "1qaz@WSX", "username": "+8613010001095"}
}

##GET请求
ucex_withTotalRecordsCountcurrent_inputdata ={
    1:{
        "urlparameter":"",
        "body":{}},
    2:{
        "urlparameter":"",
        "body":{}},
    3:{
        "urlparameter":"",
        "body":{}},
}


##GET响应body
ucex_withTotalRecordsCountcurrent_outputdata={
    1: {"httpcode":200,  "code":200, "result": "Success","data":{"orders":[]}},
    2: {"httpcode":200,  "code":200, "result": "Success","data":{"orders":[]}},
    3: {"httpcode": 200, "code":200, "result": "Success","data":{"orders": []}}
}


