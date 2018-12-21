#coding:utf-8
'''
title:  报文头和token处理
author:Robert
date:20180820
email:robert_luo1949@163.com
other:
'''

import requests,json
from qaplatform.controller.log import logger


class PackgingToken(object):
    '''

    '''

    def __init__(self,url,data,headers,clienttype):
        self.__url = url
        self.__data = data
        self.__headers = headers
        self.__clienttype = clienttype


###不抽象在类中的代码写法
    # def gettokenvalue(self,url,data,headers,clienttype):
    #     '''
    #      获取 token的值
    #     :param url:
    #     :param data:
    #     :param headers:
    #     :param clienttype:
    #     :return: tokenvalue
    #     '''
    #
    #
    #     try:
    #         logger.logger.info("doing  get tokenvalue ")
    #         response_content = requests.post(url, data=json.dumps(data), headers=headers)
    #         response_output_data = response_content.json()
    #         logger.logger.info(str(response_output_data))
    #
    #         # tokenvalue  =response_content.headers.get('ucex-web-api-token')
    #         tokenvalue = response_content.headers.get(clienttype)
    #         logger.logger.info("token value  create:  "+str(tokenvalue))
    #     except BaseException as be:
    #         logger.logger.exception("baseexception  "+str(BaseException))
    #     except Exception as e:
    #         logger.logger.exception("Exception "+str(e))
    #
    #     return tokenvalue
###不抽象在类中的代码写法


    def gettokenvalue(self):
        '''
         获取 token的值
        '''

        try:
            logger.logger.debug("doing  get tokenvalue ")
            response_content = requests.post(self.__url, data=json.dumps(self.__data), headers=self.__headers)
            response_output_data = response_content.json()
            logger.logger.debug(str(response_output_data))

            # tokenvalue  =response_content.headers.get('ucex-web-api-token')
            tokenvalue = response_content.headers.get(self.__clienttype)
            logger.logger.debug("token value  create:  "+str(tokenvalue))
        except BaseException as be:
            logger.logger.error(" 生成 token 失败")
            logger.logger.exception("baseexception  "+str(BaseException))
        except Exception as e:
            logger.logger.error(" 生成 token 失败")
            logger.logger.exception("Exception "+str(e))
        return tokenvalue


class PackgingHeaader(object):
    '''
    获取HEADER
    '''
    def __init__(self, contenttype, clienttype):
        '''

        :param contenttype:
        :param clienttype:
        '''
        self.__contenttype = contenttype
        self.__clienttype = clienttype

    def setheader(self):
        '''
         设定 header
        '''
        header =None

        try:
            header = {'Content-Type': self.__contenttype, 'request-client-type': self.__clienttype}
            logger.logger.debug("HEADER "+str(header))
        except BaseException as be:
            logger.logger.exception("BaseException  "+str(BaseException))
        except Exception as e:
            logger.logger.exception("Exception "+str(e))

        return header




