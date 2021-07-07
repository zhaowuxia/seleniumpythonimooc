import sys
import os
import HTMLTestRunner
sys.path.append("D:\\python")
from business.register_business import registerbusiness
from selenium import webdriver
import unittest
from log.user_log import userlog

class Firstcase(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.file_name="D:\\python\\util\\1.png"
        cls.log = userlog()
        cls.logger = cls.log.get_log()
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("http://www.5itest.cn/register")
        self.logger.info("this ischrome")
        self.login = registerbusiness(self.driver)
    def tearDown(self):
        for method_name,error in self._outcome.errors:#拿到当前错误case以及运行信息，是一个list
            if error:#判断error有没有
                case_name = self._testMethodName#拿到case的名字
                file_path = os.path.join(os.getcwd() + "\\report\\" + case_name+".png")
                self.driver.save_screenshot(file_path)#以case的名字命名截图
        self.driver.close()
        print("后置条件")
    @classmethod
    def tearDownClass(cls):
        cls.log.close_handle()
    def test_login_email_error(self):
        email_error = self.login.login_email_error('1314@qq.com','user1111','1111',self.file_name)
        return self.assertFalse(email_error,"测试失败")
        #if email_error==True:
            #print("注册成功，此条case失败")
        #通过assert判断是否为false
    def test_login_username_error(self):
        username_error=self.login.login_name_error('43@qq.com',"12",'1111',self.file_name)
        return self.assertFalse(username_error)
    def test_login_password_error(self):
        password_error=self.login.password_error('43@qq.com','ss',"1",self.file_name)
        return self.assertFalse(password_error)
    def test_login_code_error(self):
        code_error=self.login.code_error('43@qq.com','ss',"1",self.file_name)
        return self.assertFalse(code_error)
    def test_login_success(self):
        success = self.login.user_base('43@qq.com','ss',"1123",self.file_name)
        return self.assertFalse(success)

'''
def main():
    first = Firstcase()
    first.test_login_code_error()
    first.test_login_email_error()
    first.test_login_password_error()
    first.test_login_username_error()
    first.test_login_success()
'''
if __name__ == '__main__':
    file_path = os.path.join(os.getcwd()+"\\report\\"+'first_case.html')
    f = open(file_path,"wb")
    suite = unittest.TestSuite()
    suite.addTest(Firstcase('test_login_email_error'))
    suite.addTest(Firstcase('test_login_success'))
    runner = HTMLTestRunner.HTMLTestRunner(stream=f,title="this is first report",description="这是第一份测试报告",verbosity=2)
    runner.run(suite)


