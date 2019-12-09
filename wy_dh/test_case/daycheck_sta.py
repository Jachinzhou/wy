# -*-coding:utf-8-*-
import unittest
from time import sleep
import unittest, random, sys

sys.path.append("./models")
sys.path.append("./page_obj")
from wy_dh.test_case.models import myunit, function
from wy_dh.test_case.page_obj.ContractMPage import *
from wy_dh.test_case.page_obj.DayCheckPage import *
from wy_dh.test_case.page_obj.loginPage import login


class DayCheck(myunit.MyTest):
    def test_daycheck(self):
        '''新增抄表'''
        imgpath = r'C:/Users/admin/PycharmProjects/wy/wy_dh/data/contact.jpg'
        DayCheckPage(driver).day_check(imgpath)
