# coding:utf-8
'''
title: 自动化测试 UCEX
author:Robert
date:20180504
email:shuibo.luo@ucextech.com
content:  配置文件
other:
'''
import os,sys,datetime


####服务启动的主机名,端口号,DEBUG模式开关
HOST_NAME = "192.168.1.108"
HOST_PORT = "5000"
HOST_DEBUG_MODE = True

##远程服务的域名
ENV_DOMAINNAME ="http://bigerqa.ccx123.com/"     ##QA环境的

###启动加载目录配置D:\\Coding\\qaplatform
RUN_HOME_PATH="D:\\Coding\\qaplatform\\"
template_dir=RUN_HOME_PATH+"qaplatform\\templates"    #模板目录
static_dir=RUN_HOME_PATH+"qaplatform\\static"         #项目静态资源目录

####LOG 配置
LOG_LEVEL="DEBUG"
OBJ_LOGGER="[smoke test]"
FILE_LOGGER=RUN_HOME_PATH+"tmp\\logs\\qaplatform"+str(datetime.datetime.now().strftime("%Y%m%d"))+".log"

###临时结果集
temp_result={}


####报告配置  [0,1,2]  (0 : 冒烟测试 1 )

REPORT_INFO ={
    0:{
        "type_id":"01",                                ##类型编号
        "re_dir":RUN_HOME_PATH+"tmp\\reports\\",       ##报告存放目录
        "re_name":"example_test_"+str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))+".html",  ##报告名称
        "re_title" : "example test",            ##报告标题
        "re_description" : "example test",      ##报告描述
        "re_author" : "Robert"                ##作者
        },
    1:{
        "type_id": "01",  ##XXX类型编号
        "re_dir": RUN_HOME_PATH+"tmp\\reports\\",  ##报告存放目录
        "re_name": "smoke_test_" + str(datetime.datetime.now().strftime("%Y%m%d%H%M%S")) + ".html",  ##报告名称
        "re_title": "smoke test",  ##报告标题
        "re_description": "smoke test",  ##报告描述
        "re_author": "Robert"  ##作者
    }
}

###邮件发送配置
EMAIL_SERVER = {
    0:{    ##冒烟测试的邮件配置
        "mail_host" : "smtp.exmail.qq.com",       # SMTP服务器
        "mail_user" : "2731541089@qq.com",  # 用户名
        ##mail_pass = "robert1949"  # 授权密码，非登录密码
        "mail_pass" : "1qaz@WSX",                # 登录密码
        "sender" : '2731541089@qq.com',    # 发件人邮箱(最好写全, 不然会失败)
        "receivers" :['240505723@qq.com'],  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        "content" : 'smoke test',   ###预置的内容
        "title" : 'Smoke Test [内含报告地址Report Url]'  # 邮件主题
    },
    1:   ##XXXX测试的邮件配置
        {
        # 第三方 SMTP 服务
        "mail_host": "smtp.exmail.qq.com",  # SMTP服务器
        "mail_user": "xxx@163.com",  # 用户名
        ##mail_pass = "robert1949"  # 授权密码，非登录密码
        "mail_pass": "xxxxxxx",  # 登录密码
        "sender": '240505723@qq.com',  # 发件人邮箱(最好写全, 不然会失败)
        "receivers": ['240505723 @qq.com', 'xxxxxxx.com'],  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        "content": '我用Python',
        "title": '优雅,简洁的python'  # 邮件主题
    }
}
