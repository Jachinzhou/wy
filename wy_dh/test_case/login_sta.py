# -*-coding:utf-8-*-
import unittest
from time import sleep
import unittest, random, sys
sys.path.append("./models")
sys.path.append("./page_obj")
from wy_dh.test_case.models import myunit, function
from wy_dh.test_case.page_obj.loginPage import login

class loginTest(myunit.MyTest):

    def user_login_verify(self,username='root',password='123'):
        print(1)
        login(self.driver).user_login(username,password)
        function.insert_img(self.driver,'user_login_verify.jpg')


if __name__ == '__main__':
    unittest.main()