

import config
##url_login 登录接口
url_login = config.ENV_DOMAINNAME+"exchange/users/api/login"
url_logined =config.ENV_DOMAINNAME+\
                          "/exchange/orders/get/orderId/"

##post_requests header
t_headers_login = {'Content-Type': 'application/json', 'request-client-type': 'web'}
t_headers_order ={'Content-Type': 'application/json', 'ucex-web-api-token': None}

##post_requests token_type
token_clienttype = "ucex-web-api-token"
token_user = {
    1: {"email": "+8613010001005", "password": "1qaz@WSX", "username": "+8613010001005"},
    2: {"email": "+8613010001005", "password": "1qaz@WSX", "username": "+8613010001005"},
    3: {"email": "+8613010001005", "password": "1qaz@WSX", "username": "+8613010001005"},
    4: {"email": "+8613010001005", "password": "1qaz@WSX", "username": "+8613010001005"}
}

##GET请求
ucex_inputdata ={
    1:{
        "urlparameter":"78ac0c28-4640-48ab-8c12-48da4ca42a0d",   ##FILLED
        "body":{}},
    2:{
        "urlparameter":"76c98c25-4d86-4539-957a-03abc163f37c",   ##CANCELED
        "body":{}},
    3:{
        "urlparameter":"a7f1e0a2-372a-41ae-a24b-40f15130dad3",    ##NEW
        "body":{}},
}


##GET响应body
ucex_outputdata={
    1: {"httpcode":200,  "code":200, "result": "Success","data":{"orderState":"FILLED"}},
    2: {"httpcode":200,  "code":200, "result": "Success","data":{"orderState":"CANCELED"}},
    3: {"httpcode": 200, "code":200, "result": "Success","data":{"orderState":"NEW"}}
}


