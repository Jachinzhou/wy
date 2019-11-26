from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os

def new_report(testreport):
    lists = os.listdir(testreport)
    lists.sort(key=lambda fn: os.path.getmtime(testreport +'\\' + fn))
    file_new = os.path.join(testreport,lists[-1])
    print(file_new)
    return file_new

if  __name__ == '__main__':
    now = time.strftime('%Y-%m-%d-%H_%M_%S')
    filename = './' + now + ' result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='物业管理测试报告',
                            description='环境 :windows 10 浏览器:chrome')
    discover = unittest.defaultTestLoader.discover('./wy_dh/test_case',
                                                   pattern='*_sta.py')
    runner.run(discover)
    fp.close()
    file_path = new_report('./wy_dh/report')