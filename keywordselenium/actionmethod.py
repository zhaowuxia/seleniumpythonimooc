from selenium import webdriver
from base.find_element import FindElement
import time
class actionmethod:
    #打开浏览器
    def open_browser(self,browser):
        if browser=="chrome":
            self.driver = webdriver.Chrome()
        else:
            self.driver = webdriver.Firefox()
    #打开url
    def get_url(self,url):
        self.driver.get(url)
    #定位元素
    def find_element(self,key):
        element=FindElement(self.driver).get_element(key)
        return element
    #输入元素
    def send_key(self,value,key):
        element = self.find_element(key)
        element.send_keys(value)
    #点击元素
    def click_element(self,key):
        element = self.find_element(key).click()
    #等待
    def sleep_time(self):
        time.sleep(3)
    #关闭浏览器
    def close_browser(self):
        self.driver.close()

    # 获取title
    def get_title(self):
        title = self.driver.title
        return title
