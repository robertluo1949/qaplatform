import os,sys,datetime



####服务启动的主机名,端口号,DEBUG模式开关
HOST_NAME = "192.168.190.35"
HOST_PORT = "5000"
HOST_DEBUG_MODE = True

##远程服务的域名
ENV_DOMAINNAME ="http://bigerqa.ccx123.com/"     ##QA环境的

###启动加载目录配置
template_dir="/data/Qatest_Smoke/qaplatform/templates"    #模板目录
static_dir="/data/Qatest_Smoke/qaplatform/static"         #项目静态资源目录

####LOG 配置
LOG_LEVEL="DEBUG"
OBJ_LOGGER="[smoke test]"
FILE_LOGGER="/data/logs/qaplatform.log"


####报告配置_smoke


####报告配置  [0,1,2]  (0 : 冒烟测试 1 )

REPORT_INFO ={
    0:{
        "type_id":"01",                                ##类型编号
        "re_dir":"/data/reports/",       ##报告存放目录
        "re_name":"smoke_test_"+str(datetime.datetime.now().strftime("%Y%m%d%H%M%S"))+".html",  ##报告名称
        "re_title" : "smoke test",            ##报告标题
        "re_description" : "smoke test",      ##报告描述
        "re_author" : "Robert"                ##作者
        },
    1:{
        "type_id": "01",  ##类型编号
        "re_dir": "d:\\autotestrobot\\reports\\",  ##报告存放目录
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
        "mail_user" : "robert_luo1949@163.com",  # 用户名
        ##mail_pass = "robert1949"  # 授权密码，非登录密码
        "mail_pass" : "1qaz@WSX",                # 登录密码
        "sender" : 'robert_luo1949@163.com',    # 发件人邮箱(最好写全, 不然会失败)
        "receivers" :['robert_luo1949@163.com','240505723@qq.com','jinjing.zhang@ucextech.com','xiaohui.yang@ucextech.com'],  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        "content" : 'smoke test',
        "title" : 'Smoke Test [内含报告地址Report Url]'  # 邮件主题
    },
    1:   ##XXXX测试的邮件配置
        {
        # 第三方 SMTP 服务
        "mail_host": "smtp.exmail.qq.com",  # SMTP服务器
        "mail_user": "robert_luo1949@163.com",  # 用户名
        ##mail_pass = "robert1949"  # 授权密码，非登录密码
        "mail_pass": "1qaz@WSX",  # 登录密码
        "sender": 'robert_luo1949@163.com',  # 发件人邮箱(最好写全, 不然会失败)
        "receivers": ['robert_luo1949@163.com','240505723@qq.com','jinjing.zhang@ucextech.com'],  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱
        "content": '我用Python',
        "title": '人生苦短'  # 邮件主题
    }
}

