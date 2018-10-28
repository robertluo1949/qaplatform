# coding:utf-8
'''
title: 自动化测试 biger
author:Robert
date:20180504
email:shuibo.luo@ucextech.com
content:  java user-userlogin_101
other:
'''

from flask import  Flask
from flask import render_template
import config
import os,sys,json
import importlib
from qaplatform.controller.libs.email import sendemail
from qaplatform.controller.libs.htmlreport.HTMLTestReportCN import HTMLTestRunner
from qaplatform.controller.log import logger
from qaplatform.testmodel.bigerSmokeTest import modelSuite


app = Flask(__name__,static_folder=config.static_dir,template_folder=config.template_dir)


testre ="shuibo.luo@ucextech.com,240505723@qq.com"
@app.route('/')


# @app.route('/indextmp')
#
# def first_flask():
#     user = {'nickname' : 'Robert'}
#     return '''
#
# <html>
#   <head>
#     <title>Home Page</title>
#   </head>
#   <body>
#     <h1>Hello, ''' + user['nickname'] + '''</h1>
#   </body>
# </html>
# '''

@app.route('/index.html')

def indextmp():
    logger.logger.info("testing logger")
    return render_template("index.html")



@app.route('/test/smoke',methods=['POST','GET'])
def testsmoke():
    logger.logger.info("smoke test")


    importlib.reload(config)
    filePath = config.REPORT_INFO[0]["re_dir"] +config.REPORT_INFO[0]["re_name"]
    logger.logger.info( "生成的报告路径  " +filePath)

    with open(filePath, mode="wb") as fp:
        '''
        #生成报告的Title,描述
        '''
        runner =HTMLTestRunner(
            stream=fp,
            title=config.REPORT_INFO[0]["re_title"],
            description=config.REPORT_INFO[0]["re_description"],
            tester=config.REPORT_INFO[0]["re_author"]
        )
        modol = modelSuite()
        testsuite = modol.SuiteMulti()
        runner.run(testsuite)
        # 关闭文件，否则会无法生成文件
        fp.close()
        logger.logger.info("smoke test OK  ")
    result_json = {"Report  dir": filePath,
                   "Report  url": str(config.HOST_NAME+"/"+config.REPORT_INFO[0]["re_name"])}

    print(fp)

    try:
        sendemail.sendemailSMTP(
            config.EMAIL_SERVER[0]["mail_host"],    ##邮件发送SMTP host
            config.EMAIL_SERVER[0]["mail_user"],    ##邮件发送SMTP  user name
            config.EMAIL_SERVER[0]["mail_pass"],    ##邮件发送SMTP  user password
            config.EMAIL_SERVER[0]["receivers"],    ##邮件  收件人
            config.EMAIL_SERVER[0]["title"],        ##邮件  标题
            str(json.dumps(result_json))            ##邮件  内容
        )
        logger.logger.info(str("FROM  "+config.EMAIL_SERVER[0]["mail_host"] +" To  "+ str(config.EMAIL_SERVER[0]["receivers"])))
    except BaseException as be:
        logger.logger.exception("FROM  "+str(config.EMAIL_SERVER[0]["mail_host"]))


    return json.dumps(result_json)



if __name__=='__main__':
    app.run(host=config.HOST_NAME, port=config.HOST_PORT, debug=config.HOST_DEBUG_MODE,load_dotenv=True)