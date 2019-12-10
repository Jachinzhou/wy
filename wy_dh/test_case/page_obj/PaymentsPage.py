from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from wy_dh.test_case.page_obj.base import Page
from wy_dh.test_case.models.DataLoad import *
from wy_dh.test_case.models import function
from time import sleep
import random


class PaymentsPage(Page):
    '''基站'''
    url = '/payments/load'

    query_incode_loc = (By.XPATH, '//*[@id="innerCode"]')  # 查询合同档案号

    def query_incode(self, innerCode):
        self.find_element(*self.query_incode_loc).clear()
        self.find_element(*self.query_incode_loc).send_keys(innerCode)

    query_payments_status_loc = (By.XPATH, '//*[@id="queryForm"]/select[3]')  # 查询付款状态

    def query_payments_status(self, payments_status):
        Select(self.find_element(*self.query_payments_status_loc)).select_by_visible_text(payments_status)

    query_button_loc = (By.XPATH, '//*[@id="queryForm"]/input[13]')  # 查询按钮

    def query_button(self):
        self.find_element(*self.query_button_loc).click()

    select_paymentsDataTable_loc = (By.XPATH, '//*[@id="paymentsDataTable"]/tbody/tr[1]')  # 付款列表第一个

    def select_tenements(self):
        self.find_element(*self.select_paymentsDataTable_loc).click()

    PayBefore_Button_loc = (By.XPATH, '//*[@id="rightButton"]/button[6]')  # 支付前回访按钮

    def PayBefore_Button(self):
        self.find_element(*self.PayBefore_Button_loc).click()

    PayBefore_submit_loc = (By.XPATH, '//*[@id="popwnd_Payments_paybefore"]/div[2]/div/div[2]/button')  # 支付前回访弹窗提交按钮

    def PayBefore_submit(self):
        self.find_element(*self.PayBefore_submit_loc).click()

    # 支付前回访
    def PayBefore(self,
                  innerCode='innerCode'
                  ):
        self.query_incode(innerCode)
        self.query_payments_status('付款前回访')
        self.query_button()
        sleep(1)
        self.select_tenements()
        self.PayBefore_Button()
        self.PayBefore_submit()
        sleep(1)
        self.alert_accprt()

    payments_edit_button_loc = (By.XPATH, '//*[@id="rightButton"]/button[4]')  # 编辑按钮

    def payments_edit_button(self):
        self.find_element(*self.payments_edit_button_loc).click()

    payments_pass_button_loc = (By.XPATH, '//*[@id="mForm"]/table/tbody/tr[10]/td/div/input[2]')  # 审核通过按钮

    def payments_pass_button(self):
        self.find_element(*self.payments_pass_button_loc).click()

    def payments_pass(self, innerCode='innerCode'):
        self.query_incode(innerCode)
        self.query_payments_status('等待审核')
        self.query_button()
        sleep(1)
        self.select_tenements()
        self.payments_edit_button()
        self.payments_pass_button()
        sleep(1)
        self.alert_accprt()
        sleep(1)
        self.alert_accprt()
    


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://wy.dhwl66.com:8001/dhwy/passport/login')
    driver.find_element_by_id('username').send_keys('周继成')
    driver.find_element_by_id('password').send_keys('12345678')
    driver.find_element_by_id('loginSub').click()
    sleep(1)
    other_windowns_url = 'http://wy.dhwl66.com:8001/dhwy/payments/load'
    PaymentsPage(driver).open_other_windowns(other_windowns_url, 1)
    sleep(1)
    PaymentsPage(driver).payments_pass('201912094048')

    driver.quit()
