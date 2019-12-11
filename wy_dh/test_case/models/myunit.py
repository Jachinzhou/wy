from selenium import webdriver
from .driver import brower
import unittest
from time import sleep
import os
from wy_dh.test_case.page_obj.loginPage import login
from wy_dh.test_case.models.DataLoad import ExcelReader


class MyTest(unittest.TestCase):
    def setUp(self):
        self.driver = brower()
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        login(self.driver).user_login(username='周继成', password='12345678')
        sleep(1)
        self.driver.execute_script("window.open('http://wy.dhwl66.com:8001/dhwy/contracts/load')")
        self.driver.get('http://wy.dhwl66.com:8001/dhwy/contracts/load')
        # print(self.driver.window_handles)  # 打印当前所有窗口
        self.driver.switch_to.window(self.driver.window_handles[1])  # 切换到新打开的窗口
        sleep(2)

    def tearDown(self):
        sleep(3)
        self.driver.quit()
