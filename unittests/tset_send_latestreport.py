# -*- coding: utf-8 -*-
# @Time    : ${DATE} ${TIME}
# @Author  : Aries
# @Site    : ${SITE}
# @File    : ${NAME}.py
# @Software: ${PRODUCT_NAME}

import sys,os
##先把父级目录加入python运行的环境变量
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
print(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


import config
from qaplatform.controller.libs.email import sendemailreport

print("****  ",str(config.REPORT_INFO[0]["re_dir"]),str(config.EMAIL_SERVER[0]["type_id"]))
sr =sendemailreport.SendReport(str(config.REPORT_INFO[0]["re_dir"]),
                 0)
sr.send_mail_html()



