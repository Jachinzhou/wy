# -*-coding:utf-8-*-
import unittest
from time import sleep
import unittest, random, sys

sys.path.append("./models")
sys.path.append("./page_obj")
from wy_dh.test_case.models import myunit, function
from wy_dh.test_case.page_obj.loginPage import login


class loginTest(myunit.MyTest):
    '''登陆测试'''

    def user_login_verify(self, username='', password=''):
        login(self.driver).user_login(username, password)

    def test_login1(self):
        '''用户名正确，密码错误'''
        self.user_login_verify(username='root', password='1234')
        sleep(1)
        po = login(self.driver).login_alert()
        # po = self.driver.switch_to_alert()
        self.assertEqual(po.text, '密码错误')
        function.insert_img(self.driver, 'test_login1.png')
        po.accept()


    # def test_login2(self):
    #     '''用户名错误，密码正确'''
    #     self.user_login_verify(username='root1', password='123')
    #     sleep(1)
    #     po = login(self.driver).login_alert()
    #     # po = self.driver.switch_to_alert()
    #     self.assertEqual(po.text, '用户不存在')
    #     po.accept()
    #     function.insert_img(self.driver, 'test_login2.png')
    #
    # def test_login3(self):
    #     '''用户名空，密码空'''
    #     self.user_login_verify(username='', password='')
    #     sleep(1)
    #     po = login(self.driver).login_alert()
    #     # po = self.driver.switch_to_alert()
    #     self.assertEqual(po.text, '您未填写用户名！')
    #     po.accept()
    #     function.insert_img(self.driver, 'test_login3.png')
    #
    # def test_login4(self):
    #     '''用户名正确，密码空'''
    #     self.user_login_verify(username='root', password='')
    #     sleep(1)
    #     po = login(self.driver).login_alert()
    #     # po = self.driver.switch_to_alert()
    #     self.assertEqual(po.text, '您未填写密码！')
    #     po.accept()
    #     function.insert_img(self.driver, 'test_login4.png')
    #
    # def test_login5(self):
    #     '''用户名正确，密码正确'''
    #     self.user_login_verify(username='周继成', password='12345678')
    #     function.insert_img(self.driver, 'test_login5.png')


if __name__ == '__main__':
    unittest.main()
