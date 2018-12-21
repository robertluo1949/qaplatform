# -*- coding: utf-8 -*-

# 发送html内容的邮件
import smtplib, time, os
import config
from email.mime.text import MIMEText
from email.header import Header

class SendReport(object):
    '''

    '''
    def __init__(self,dir,TESTTYPE):
        self.TESTTYPE =TESTTYPE
        self.dir=dir
        print(self.dir,self.TESTTYPE)

    def find_new_file(self):
        '''查找目录下最新的文件'''
        file_lists = os.listdir(self.dir)
        file_lists.sort(key=lambda fn: os.path.getmtime(self.dir + "\\" + fn)
                        if not os.path.isdir(self.dir + "\\" + fn)
                        else 0)
        # print('最新的文件为： ' + file_lists[-1])
        file = os.path.join(self.dir, file_lists[-1])
        print('完整文件路径：', file)
        return file


    def send_mail_html(self):
        '''发送html内容邮件'''

        sendfile =self.find_new_file()
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())

        smtpserver =config.EMAIL_SERVER[self.TESTTYPE]["mail_host"],  ##邮件发送SMTP host
        # username =config.EMAIL_SERVER[self.TESTTYPE]["mail_user"],  ##邮件发送SMTP  user name
        sender =config.EMAIL_SERVER[self.TESTTYPE]["sender"],  ##邮件发送SMTP  发件人

        # password =config.EMAIL_SERVER[self.TESTTYPE]["mail_passwd"],  ##邮件发送SMTP  user password
        # receiver = config.EMAIL_SERVER[self.TESTTYPE]["receivers"],  ##邮件  收件人
        # subject =str(config.EMAIL_SERVER[self.TESTTYPE]["title"] +t),  ##邮件  标题

        # str(json.dumps(result_json))            ##邮件  内容
        # message
        # 发送邮箱
        # sender = '240505723@qq.com'
        # 接收邮箱
        receiver = '2731541089@qq.com'
        # 发送邮件主题
        t = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        subject = '自动化测试结果_' + t
        # 发送邮箱服务器
        smtpserver = 'smtp.qq.com'
        # 发送邮箱用户/密码
        username = '240505723'
        password = 'xxxxxxxxx'

        # 读取html文件内容
        f = open(sendfile, 'rb')
        mail_body = f.read()
        f.close()

        # 组装邮件内容和标题，中文需参数‘utf-8’，单字节字符不需要
        msg = MIMEText(mail_body, _subtype='html', _charset='utf-8')
        msg['Subject'] = Header(subject, 'utf-8')
        msg['From'] = sender
        msg['To'] = receiver
        # 登录并发送邮件
        try:
            smtp = smtplib.SMTP()
            smtp.connect(smtpserver)
            smtp.login(username, password)
            smtp.sendmail(sender, receiver, msg.as_string())
        except IOError  as ioe:
            print("邮件发送失败！",ioe)
        except Exception as e:
            print("邮件发送失败！",e)
        else:
            print("邮件发送成功！")
        finally:
            smtp.quit()




# dir = 'D:\\Coding\qaplatform\\tmp\\reports\\'  # 指定文件目录
# file = find_new_file(dir)  # 查找最新的html文件
# send_mail_html(file)  # 发送html内容邮件