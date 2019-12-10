from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from wy_dh.test_case.page_obj.base import Page
from wy_dh.test_case.models.DataLoad import *
from wy_dh.test_case.models import function
from time import sleep
import random


class TenementsPage(Page):
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

    add_tenementammeters_button_loc = (
        By.XPATH, '//*[@id="popwnd_Tenements_edit"]/div[2]/div[1]/div[2]/button')  # 电表管理按钮

    def add_tenementammeters_button(self):
        self.find_element(*self.add_tenementammeters_button_loc).click()

    reimbursements_tab_loc = (By.XPATH, '//*[@id="tabs"]/ul/li[2]')  # 报账填写页面

    def reimbursements_tab(self):
        self.find_element(*self.reimbursements_tab_loc).click()

    customer_service_tab_loc = (By.XPATH, '//*[@id="tabs"]/ul/li[1]')  # 报账填写页面

    def customer_service_tab(self):
        self.find_element(*self.customer_service_tab_loc).click()

    input_chinaCode_loc = (By.XPATH, '//*[@id="tabs"]/table/tbody/tr/td/input')  # 移动电表编号

    def input_chinaCode(self, chinaCode):
        self.find_element(*self.input_chinaCode_loc).clear()
        self.find_element(*self.input_chinaCode_loc).send_keys(chinaCode)

    input_chinaMobileInitNumber_loc = (By.XPATH, '//*[@id="account"]/table/tbody/tr[1]/td/input')  # 移动提供的初始化数据

    def input_chinaMobileInitNumber(self, chinaMobileInitNumber):
        self.find_element(*self.input_chinaMobileInitNumber_loc).clear()
        self.find_element(*self.input_chinaMobileInitNumber_loc).send_keys(chinaMobileInitNumber)

    input_lastNumber_loc = (By.XPATH, '//*[@id="account"]/table/tbody/tr[2]/td/input')  # 月平均用电量

    def input_lastNumber(self, lastNumber):
        self.find_element(*self.input_lastNumber_loc).clear()
        self.find_element(*self.input_lastNumber_loc).send_keys(lastNumber)

    input_lastCheckoutDate_loc = (By.XPATH, '//*[@id="lastCheckoutDate"]')  # 移动结算的截止日期

    def input_lastCheckoutDate(self, lastCheckoutDate):
        self.find_element(*self.input_lastCheckoutDate_loc).clear()
        self.find_element(*self.input_lastCheckoutDate_loc).send_keys(lastCheckoutDate)

    input_ratio_loc = (By.XPATH, '//*[@id="account"]/table/tbody/tr[4]/td/input')  # 倍率

    def input_ratio(self, ratio):
        self.find_element(*self.input_ratio_loc).clear()
        self.find_element(*self.input_ratio_loc).send_keys(ratio)

    Submit_button_loc = (By.XPATH, '//*[@id="Submit"]')  # 新增物业单位电表提交按钮

    def submit_tenementammeters(self):
        self.find_element(*self.Submit_button_loc).click()

    def add_tenementammeters(self,
                             innerCode='innerCode',
                             chinaCode='chinaCode',
                             chinaMobileInitNumber='chinaMobileInitNumber',
                             lastNumber='lastNumber',
                             lastCheckoutDate='lastCheckoutDate',
                             ratio='ratio'
                             ):
        self.query_incode(innerCode)
        self.query_button()
        self.select_tenements()
        self.ammeters_edit_button()
        self.add_tenementammeters_button()
        self.reimbursements_tab()
        self.input_chinaCode(chinaCode)
        self.input_chinaMobileInitNumber(chinaMobileInitNumber)
        self.input_lastNumber(lastNumber)
        self.input_lastCheckoutDate(lastCheckoutDate)
        self.input_ratio(ratio)
        self.customer_service_tab()
        self.submit_tenementammeters()
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
    other_windowns_url = 'http://wy.dhwl66.com:8001/dhwy/tenements/load'
    TenementsPage(driver).open_other_windowns(other_windowns_url)
    # driver.execute_script("window.open('http://wy.dhwl66.com:8001/dhwy/tenements/load')")
    # driver.switch_to_window(driver.window_handles[1])  # 切换到新打开的窗口
    sleep(1)
    TenementsPage(driver).query_incode('201912034005')
    TenementsPage(driver).query_button()
    TenementsPage(driver).select_tenements()
    TenementsPage(driver).ammeters_edit_button()
    TenementsPage(driver).add_tenementammeters_button()
    TenementsPage(driver).reimbursements_tab()
    TenementsPage(driver).input_chinaCode(random.randint(0000000000, 9999999999))
    TenementsPage(driver).input_chinaMobileInitNumber(random.randint(0000, 9999))
    TenementsPage(driver).input_lastNumber(random.randint(000, 999))
    TenementsPage(driver).input_lastCheckoutDate('2019-07-01')
    TenementsPage(driver).input_ratio('2')
    TenementsPage(driver).customer_service_tab()
    TenementsPage(driver).submit_tenementammeters()
    sleep(1)
    TenementsPage(driver).alert_accprt()

    sleep(2)
    driver.quit()
