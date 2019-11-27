from selenium.webdriver import Remote
from selenium import webdriver


# 启动浏览器
def brower():
    driver = webdriver.Chrome()
    return driver


if __name__ == '__main__':
    dr = brower()
    dr.get('http://192.168.18.148:8080/dhwy/passport/login')
    dr.quit()
