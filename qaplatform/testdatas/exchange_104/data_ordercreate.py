

import config
##url_login 登录接口
url_login = config.ENV_DOMAINNAME+"exchange/users/api/login"
url_exchangeorderscreate =config.ENV_DOMAINNAME+"exchange/orders/create"

##post_requests header
t_headers_login = {'Content-Type': 'application/json', 'request-client-type': 'web'}
t_headers_order ={'Content-Type': 'application/json', 'ucex-web-api-token': None}

##post_requests token_type
token_clienttype = "ucex-web-api-token"
token_user = {
  1:{"email":"+8613010001095","password":"1qaz@WSX","username":"+8613010001095"},
  2:{"email":"+8613010001095","password":"1qaz@WSX","username":"+8613010001093"},
  3: {"email": "+8613010001003", "password": "1qaz@WSX", "username": "+8613010001003"},
  4: {"email": "+8613010001003", "password": "1qaz@WSX", "username": "+8613010001003"}
}

##POST请求body 买入 BUY
ucex_exchangeorderscreate_inputdata ={
    1:{
        "urlparameter":"",
        "body":{"currency": "BTC","orderQty": 0.1,"orderType": "Limit",\
         "price": 2,"side": "BUY","symbol": "LTCBTC","userId": "7199"}},
    2:{
        "urlparameter":"",
        "body":{
        "currency": "BTC","orderQty": 0.1,"orderType": "Limit",\
        "price": 2,"side": "SELL","symbol": "LTCBTC","userId": "7199"}},
    3: {
        "urlparameter": "",
        "body": {
            "currency": "BTC", "orderQty": 0.1, "orderType": "Limit", \
            "price": 2, "side": "SELL", "symbol": "LTCBTC", "userId": "7199"}},
    4: {
        "urlparameter": "",
        "body": {
            "currency": "BTC", "orderQty": 0.1, "orderType": "Limit", \
            "price": 2, "side": "SELL", "symbol": "LTCBTC", "userId": "7199"}}
}



##POST响应body
ucex_exchangeorderscreate_outputdata={
    1:{"httpcode":200, "code":200, "result": "Success","data":{}},
    2:{"httpcode":200, "code":200, "result": "Success","data":{
            "orderId": "a3228d46-8864-4932-af32-0967a5f0782a",
            "clientOrderId": 11740026839761920,
            "side": "SELL",
            "sideDisplayName": "SELL",
            "symbol": "LTCBTC",
            "symbolDisplayName": "LTC/BTC",
            "baseCurrencyCode": 103,
            "baseCurrencyName": "LTC",
            "quoteCurrencyCode": 101,
            "quoteCurrencyName": "BTC",
            "orderType": "LIMIT",
            "orderState": "PENDING",
            "orderStateDisplayName": "PENDING",
            "orderStateCode": 1,
            "price": "2.000000",
            "orderQty": "0.100",
            "filledQty": "0.000",
            "totalPrice": "0.00000000",
            "fee": "0",
            "userId": 7199,
            "tradesCount": None,
            "dealPrice": "0",
            "finishedRate": "0",
            "completeTime": None,
            "createTime": 1537157124142,
            "updateTime": None,
            "rejectReason": None
        }},
    3: {"httpcode": 200, "code": 200, "result": "Success", "data": {"orderState":"PENDING","orderStateCode":"1"}},
    4: {"httpcode": 200, "code": 200, "result": "Success", "data": {"orderState":"PENDING","orderStateCode":"1"}}

}


