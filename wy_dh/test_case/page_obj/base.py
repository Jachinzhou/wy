from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class Page(object):
    """
    BasePage封装所有页面都公用的方法，例如driver, url ,FindElement等
    """
    # 初始化driver、url、pagetitle等
    # 实例化BasePage类时，最先执行的就是__init__方法，该方法的入参，其实就是BasePage类的入参。
    # __init__方法不能有返回值，只能返回None
    # self只实例本身，相较于类Page而言。

    wy_url = 'http://wy.dhwl66.com:8001/dhwy'

    def __init__(self, selenium_driver, base_url=wy_url, parent=None):
        self.base_url = base_url
        self.driver = selenium_driver
        self.timeout = 30
        self.parent = parent

    def _open(self, url):
        url = self.base_url + url
        self.driver.get(url)
        #print(url)
        # assert self.on_page(), 'Did not land on %s' % url

    # 重写元素定位方法
    def find_element(self, *loc):
        # return self.driver.find_element(*loc)
        try:
            # 确保元素是可见的。
            # 注意：以下入参为元组的元素，需要加*。Python存在这种特性，就是将入参放在元组里。
            # WebDriverWait(self.driver,10).until(lambda driver: driver.find_element(*loc).is_displayed())
            # 注意：以下入参本身是元组，不需要加*
            WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(loc))
            return self.driver.find_element(*loc)
        except:
            print(u"%s 页面中未能找到 %s 元素" % (self, loc))

    def find_elements(self, *loc):
        return self.driver.find_elements(*loc).clear()

    def open(self):
        self._open(self.url)

    def on_page(self):
        return self.driver.current_url == (self.base_url + self.url)

    def script(self, src):
        return self.driver.execute_script(src)

    def remove_readonly(self, id):
        js = 'document.getElementById("' + id + '").removeAttribute("readonly");'
        # print(js)
        return self.driver.execute_script(js)

    def alert_accprt(self):
        alert = self.driver.switch_to_alert()
        text = alert.text
        # print(text)
        alert.accept()
        return text


if __name__ == '__main__':
    Page.remove_readonly(webdriver, 'startTime')
