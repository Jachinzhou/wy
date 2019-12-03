from HTMLTestRunner import HTMLTestRunner
from email.mime.text import MIMEText
from email.header import Header
import smtplib
import unittest
import time
import os


def send_mail(file_new):
    f = open(file_new, 'rb')
    mail_body = f.read()
    f.close()

    msg = MIMEText(mail_body, 'html', 'utf-8')
    msg['subject'] = Header('测试报告', 'utf-8')
    from_addr = '2273937910@qq.com'  # 邮件发送账号
    to_addrs = '1587739993@qq.com'  # 接收邮件账号
    qqCode = 'mgyqummajfirdifi'  # 授权码（这个要填自己获取到的）
    smtp_server = 'smtp.qq.com'  # 固定写死
    smtp_port = 465  # 固定端口

    # 配置服务器
    stmp = smtplib.SMTP_SSL(smtp_server, smtp_port)
    stmp.login(from_addr, qqCode)
    stmp.sendmail('2273937910@qq.com', '1587739993@qq.com', msg.as_string())
    stmp.quit()
    print('email has send out !')


def new_report(report):
    lists = os.listdir(report)
    lists.sort(key=lambda fn: os.path.getmtime(report + '\\' + fn))
    file_new = os.path.join(report, lists[-1])
    # print(file_new)
    return file_new



if __name__ == '__main__':
    report = 'C:/Users/admin/PycharmProjects/wy/wy_dh/report'
    now = time.strftime('%Y-%m-%d-%H_%M_%S')
    filename = report + '\\' + now + '_result.html'
    fp = open(filename, 'wb')
    runner = HTMLTestRunner(stream=fp,
                            title='物业管理测试报告',
                            description='环境 :windows 10 浏览器:chrome')
    discover = unittest.defaultTestLoader.discover('./wy_dh/test_case',
                                                   pattern='ContractM_sta.py')
    runner.run(discover)
    fp.close()
    file_path = new_report('./wy_dh/report')

    # new_report = new_report(report)
    # send_mail(new_report)
