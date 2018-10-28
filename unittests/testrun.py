# coding:utf-8
'''
title: 自动化测试 biger
author:Robert
date:20180504
email:shuibo.luo@ucextech.com
content:  java user-userlogin_101
other:
'''


from qaplatform.controller.log import logger
from qaplatform.controller.libs.htmlreport.HTMLTestReportCN import HTMLTestRunner
from qaplatform.testmodel.bigerSmokeTest import modelSuite



if __name__ == '__main__':

    re_title = "smoke test"
    re_description = "smoke test"
    re_author = "robert"

    filePath = "d:\\autotestrobot\\reports\\a.html"
    logger.logger.info( "生成的报告路径  " +filePath)

    with open(filePath, mode="wb") as fp:
        '''
        #生成报告的Title,描述
        '''

        runner =HTMLTestRunner(
            stream=fp,
            title=re_title,
            description=re_description
        )


        modol = modelSuite()
        testsuite = modol.SuiteMulti()
        runner.run(testsuite)
        # 关闭文件，否则会无法生成文件
        fp.close()