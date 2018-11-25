# coding:utf-8
'''
title: 自动化测试 UCEX
author:Robert
date:20180504
email:robert_luo1949@163.com
content:  java user-userlogin_101
other:
'''

import os
import smtplib
from email.header import Header
from email.mime.text import MIMEText
from qaplatform.controller.log import logger


def find_new_file(dir):
    '''查找目录下最新的文件'''
    file_lists = os.listdir(dir)
    file_lists.sort(key=lambda fn: os.path.getmtime(dir + "\\" + fn)
    if not os.path.isdir(dir + "\\" + fn)
    else 0)
    print('最新的文件为： ' + file_lists[-1])
    file = os.path.join(dir, file_lists[-1])
    print('完整文件路径：', file)
    return file

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
    msg = MIMEText(content, 'html', 'utf-8')
    msg['Subject'] = Header(subject, 'utf-8')  # subject
    msg['From'] = from_account
    msg['To'] = ",".join(to_account)
    # print("msg.as_string()   ",msg.as_string())
    email_client.sendmail(from_account, to_account, msg.as_bytes())

    email_client.quit()


