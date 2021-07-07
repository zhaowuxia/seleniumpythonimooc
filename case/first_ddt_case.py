import ddt
import unittest
import sys
import os
import HTMLTestRunner
sys.path.append("D:\\python")
from business.register_business import registerbusiness
from selenium import webdriver
from util.excel_util import excelutil
import time
ex = excelutil()
data = ex.get_data()
file_name="D:\\python\\util\\1.png"
#邮箱、用户名、密码、验证码、错误信息元素定位、错误信息提示
@ddt.ddt
class firstddtcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name="D:\\python\\util\\1.png"
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.login = registerbusiness(self.driver)

    def tearDown(self):
        for method_name, error in self._outcome.errors:  # 拿到当前错误case以及运行信息，是一个list
            if error:  # 判断error有没有
                case_name = self._testMethodName  # 拿到case的名字
                file_path = os.path.join(os.getcwd() + "\\report\\" + case_name + ".png")
                self.driver.save_screenshot(file_path)  # 以case的名字命名截图
        time.sleep(2)
        self.driver.close()

    '''
    @ddt.data(
        ['12', 'ss', '1111', 'code', 'username_error'],
        ['@qq.com', 'ss', '1111', 'code', 'username_error'],
        ['12qw@qq.com', 'ss', '1111', 'code', 'username_error']
    )
    @ddt.unpack
    '''
    @ddt.data(*data)
    def test_register_test(self,data):
        email,username,password,assertcode=data
        username_error=self.login.regiser_function(email,username,password,self.file_name,assertcode)
        self.assertFalse(username_error)
if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+"\\report\\"+'first_case1.html')
    f = open(file_path,"wb")
    suite = unittest.TestLoader().loadTestsFromTestCase(firstddtcase)
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="this is first report",description="这是第一份测试报告",verbosity=2)
    runner.run(suite)
