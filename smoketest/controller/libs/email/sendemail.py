# coding:utf-8
'''
title: 自动化测试 UCEX
author:Robert
date:20180504
email:shuibo.luo@ucextech.com
content:  java user-userlogin_101
other:
'''

import smtplib
from email.header import Header
from email.mime.text import MIMEText
from smoketest.controller.log import logger



def sendEmailSSL(SMTP_host, from_account, from_passwd, to_account, subject, content):
    message = MIMEText(content, 'plain', 'utf-8')  # 内容, 格式, 编码
    message['From'] = "{}".format(from_account)
    message['To'] = ",".join(to_account)
    message['Subject'] = subject

    try:
        smtpObj = smtplib.SMTP_SSL(SMTP_host, 465)  # 启用SSL发信, 端口一般是465
        smtpObj.login(from_account, from_passwd)  # 登录验证
        smtpObj.sendmail(from_account, from_passwd, message.as_string())  # 发送
        print("mail has been send successfully.")
    except smtplib.SMTPException as e:
        print(e)


def sendemailSMTP(SMTP_host, from_account, from_passwd, to_account, subject, content):
    email_client = smtplib.SMTP(SMTP_host)
    email_client.login(from_account, from_passwd)
    # create msg
    msg = MIMEText(content, 'plain', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = ",".join(to_account)
    email_client.sendmail(from_account, to_account, msg.as_string())

    email_client.quit()


