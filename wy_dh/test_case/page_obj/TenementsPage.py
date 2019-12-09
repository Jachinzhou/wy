from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from wy_dh.test_case.page_obj.base import Page
from wy_dh.test_case.models.DataLoad import *
from wy_dh.test_case.models import function
from time import sleep
import random


class ContractMPage(Page):
    '''基站'''
    url = '/tenements/load'

    query_incode_loc = (By.XPATH, '//*[@id="innerCode"]')  # 查询合同档案号

    def query_incode(self, innerCode):
        self.find_element(*self.query_incode_loc).clear()
        self.find_element(*self.query_incode_loc).send_keys(innerCode)

    query_button_loc = (By.XPATH, '//*[@id="queryForm"]/input[5]')  # 查询按钮

    def query_button(self):
        self.find_element(*self.query_button_loc).click()

    select_tenementsDataTable_loc = (By.XPATH, '//*[@id="tenementsDataTable"]/tbody/tr[1]')  # 选择物业单位列表第一个

    def select_tenements(self):
        self.find_element(*self.select_tenementsDataTable_loc).click()

    ammeters_edit_button_loc = (By.XPATH, '/html/body/div[3]/div/div[2]/button[1]')  # 电表管理按钮

    def ammeters_edit_button(self):
        self.find_element(*self.ammeters_edit_button_loc).click()

    add_tenementammeters_button_loc = (By.XPATH, '//*[@id="popwnd_Tenements_edit"]/div[2]/div[1]/div[2]/button')  # 电表管理按钮

    def add_tenementammeters(self):
        self.find_element(*self.add_tenementammeters_button_loc).click()

    reimbursements_tab_loc = (By.XPATH, '//*[@id="tabs"]/ul/li[2]')  # 报账填写页面

    def reimbursements_tab(self):
        self.find_element(*self.reimbursements_tab_loc).click()

    input_chinaCode_loc = (By.XPATH, '//*[@id="tabs"]/table/tbody/tr/td/input')  # 移动电表编号

    def input_chinaCode(self, chinaCode):
        self.find_element(*self.input_chinaCode_loc).clear()
        self.find_element(*self.input_chinaCode_loc).send_keys(chinaCode)

    input_chinaMobileInitNumber_loc = (By.XPATH, '//*[@id="account"]/table/tbody/tr[1]/td/input')  # 移动提供的初始化数据

    def input_chinaMobileInitNumber(self, chinaMobileInitNumber):
        self.find_element(*self.input_chinaMobileInitNumber_loc).clear()
        self.find_element(*self.input_chinaMobileInitNumber_loc).send_keys(chinaMobileInitNumber)

    input_lastNumber_loc = (By.XPATH, '//*[@id="account"]/table/tbody/tr[2]/td/input')  # 移动提供的初始化数据

    def input_lastNumber(self, lastNumber):
        self.find_element(*self.input_lastNumber_loc).clear()
        self.find_element(*self.input_lastNumber_loc).send_keys(lastNumber)
