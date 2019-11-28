from selenium.webdriver.common.action_chains import ActionChains
from selenium import webdriver
from selenium.webdriver.common.by import By
from wy_dh.test_case.page_obj.base import  Page
from time import sleep


class login(Page):
    '''
    登陆
    '''
    url = '/passport/login'
    wy_login_username_loc = (By.ID, 'username')
    wy_login_password_loc = (By.ID, 'password')
    wy_login_loginSub_loc = (By.ID, 'loginSub')

    def login_username(self, username):
        self.find_element(*self.wy_login_username_loc).send_keys(username)

    def login_password(self, password):
        self.find_element(*self.wy_login_password_loc).send_keys(password)

    def login_button(self):
        self.find_element(*self.wy_login_loginSub_loc).click()

    def user_login(self, username='username', password='password'):
        self.open()
        sleep(1)
        self.login_username(username)
        self.login_password(password)
        self.login_button()

    def login_alert(self):
        alert = self.driver.switch_to_alert()
        return alert

if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://192.168.18.148:8080/dhwy/contracts/load')
    login(driver).user_login('root','123')
