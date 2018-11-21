**QA 自动化测试 ---冒烟测试**  <br>
smoke Test             <br>
1   编程语言 python 3.6   <br>
2   开发框架  flask     [官方说明 http://flask.pocoo.org/]  <br>
3   平台支持  Windows 10 && Centos 7.4   <br>


**项目结构介绍**   <br>
1  qaplatform  : 项目测试案例目录 <br>
 ------------------controller : 控制器和引用libs <br>
 ------------------static : flask 基础包 静态资源 <br>
 ------------------templates : flask 基础包 模板 <br>
 ------------------testcases : 项目的测试案例包  模板 <br>
 ------------------testdatas : 项目的测试数据包   <br>
 ------------------testmodel : 项目的测试模型包   <br>
2  temp  :  保存临时文件目录     <br>
3  tests :  本项目的测试代码     <br>
4  venv  :   python3 虚拟机目录 (暂时没有)         <br>
5  config.py   项目的配置文件[日志][报告][启动参数]  <br>
6  requirements: 项目的依赖      [导出依赖命令  pip freeze > requirements.txt ] <br>
    [导入依赖命令  pip install -r requirements.txt ] <br>
7  run.py      项目启动文件 [运行命令  python run.py]   <br>


**参考引用:**    <br>
smoke test 用例清单:  http://confluence.ucex.corp/pages/viewpage.action?pageId=9208286 <br>

新手指导:    <br>
1     安装pycharm professional 并授权密钥   <br>
2     配置运行环境  python virtual machine  <br>
3     git clone 代码 https://github.com/robertluo1949/qaplatform.git <br>
4     到 smoketest指定模块目录下增加  data文件   <br>
5     编号规则[总共7位数]  前面3位是模块编号  后面4位是测试用例编号,从 101 开始 到 9999 结束. <br>  
