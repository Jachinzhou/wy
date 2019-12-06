from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.select import Select
from selenium import webdriver
from selenium.webdriver.common.by import By
from wy_dh.test_case.page_obj.base import Page
from wy_dh.test_case.models.DataLoad import *
from wy_dh.test_case.models import function
from time import sleep
import random
from datetime import datetime, date, time
from dateutil.relativedelta import relativedelta


class DayCheckPage(Page):
    select_daycheckrows_loc = (By.XPATH, '//*[@id="dayreadmeterDataTable"]/tbody/tr[1]')  # 选择物业单位列表第一个

    def select_daycheckrows(self):
        self.find_element(*self.select_daycheckrows_loc).click()

    check_button_loc = (By.XPATH, '/html/body/div[3]/div/div[2]/button[1]')  # 录入电量按钮

    def check_button(self):
        self.find_element(*self.check_button_loc).click()

    check_endTime_loc = (By.XPATH, '//*[@id="endTime"]')  # 本次抄表时间

    def input_checkendTime(self, checktime):
        self.find_element(*self.check_endTime_loc).clear()
        self.find_element(*self.check_endTime_loc).send_keys(checktime)

    this_number_loc = (By.XPATH, '//*[@id="data"]/table/tbody/tr[5]/td[2]/input')  # 本次抄表时间

    def input_checknumber(self, checknumber):
        self.find_element(*self.this_number_loc).clear()
        self.find_element(*self.this_number_loc).send_keys(checknumber)

    ele_meter_tab_loc = (By.XPATH, '//*[@id="tabs"]/ul/li[2]/a')  # 电表照片tab

    def elemeter_tab(self):
        self.find_element(*self.ele_meter_tab_loc).click()

    up_image_loc = (By.XPATH, '//*[@id="file"]')  # 电表照片tab

    def up_image(self, imgpath):
        self.find_element(*self.up_image_loc).send_keys(imgpath)

    submit_loc = (By.XPATH, '//*[@id="Submit"]')  # 提交按钮

    def submit(self):
        self.find_element(*self.submit_loc).click()

    def get_values(xpath):
        cls = driver.find_element_by_xpath(xpath)
        value = cls.get_attribute('value')
        return value

    def next_months(data):
        next_months = data + relativedelta(months=+1)
        return next_months

    def day_check(self,imgpath):
        self.select_daycheckrows()
        self.check_button()
        sleep(1)
        oldchecktime = DayCheckPage.get_values('//*[@id="startTime"]')
        checktime = DayCheckPage.next_months(date.fromisoformat(oldchecktime))
        self.remove_readonly('endTime')
        self.input_checkendTime(str(checktime))
        lastNumber = DayCheckPage.get_values('//*[@id="data"]/table/tbody/tr[5]/td[1]/input')
        this_number = int(float(lastNumber)) + random.randint(000, 999)
        self.input_checknumber(str(this_number))
        self.elemeter_tab()
        self.up_image(imgpath)
        sleep(1)
        self.submit()
        sleep(1)
        self.alert_accprt()


if __name__ == '__main__':
    imgpath = r'C:/Users/admin/PycharmProjects/wy/wy_dh/data/contact.jpg'
    e = 'C:/Users/admin/PycharmProjects/wy/wy_dh/data/合同台账2019-12-02.xlsx'
    reader = ExcelReader(e, title_line=True)
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://wy.dhwl66.com:8001/dhwy/passport/login')
    driver.find_element_by_id('username').send_keys('周继成')
    driver.find_element_by_id('password').send_keys('12345678')
    driver.find_element_by_id('loginSub').click()
    sleep(1)
    driver.get('http://wy.dhwl66.com:8001/dhwy/day/load')
    sleep(1)
    # DayCheckPage(driver).select_daycheckrows()
    # DayCheckPage(driver).check_button()
    # sleep(1)
    # oldchecktime = DayCheckPage.get_values('//*[@id="startTime"]')
    # checktime = DayCheckPage.next_months(date.fromisoformat(oldchecktime))
    # DayCheckPage(driver).remove_readonly('endTime')
    # DayCheckPage(driver).input_checkendTime(str(checktime))
    # lastNumber = DayCheckPage.get_values('//*[@id="data"]/table/tbody/tr[5]/td[1]/input')
    # this_number = int(float(lastNumber)) + random.randint(000, 999)
    # DayCheckPage(driver).input_checknumber(str(this_number))
    # DayCheckPage(driver).elemeter_tab()
    # DayCheckPage(driver).up_image(imgpath)
    # sleep(1)
    # DayCheckPage(driver).submit()
    # sleep(1)
    # DayCheckPage(driver).alert_accprt()
    # DayCheckPage(driver).day_check(imgpath)
    # driver.quit()

    text = DayCheckPage.get_values('//*[@id="dayreadmeterDataTable"]/tbody/tr[1]/td[1]')
    print(text)
