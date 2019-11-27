from selenium import webdriver
from time import sleep
import os


# 截图
def insert_img(driver, file_name):
    base_dir = os.path.dirname(os.path.dirname(__file__))
    base_dir = str(base_dir)
    base_dir = base_dir.replace('\\', '/')
    base = base_dir.split('/test_case')[0]
    file_path = base + '/report/image' + file_name
    driver.get_screenshot_as_file(file_path)


if __name__ == '__main__':
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get('http://192.168.18.148:8080/dhwy/passport/login')
    driver.find_element_by_id('username').send_keys('root')
    driver.find_element_by_id('password').send_keys('')
    driver.find_element_by_id('loginSub').click()
    insert_img(driver, 'alert.png')
    driver.switch_to.alert.accept()

    sleep(1)
    driver.quit()
