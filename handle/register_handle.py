#放login页面的操作流程
from page.register_page import registerpage
from util.get_code import getcode
class registerhandle(object):
    def __init__(self,driver):
        self.driver = driver
        self.register_p = registerpage(self.driver)
    #输入邮箱
    def send_user_email(self,email):
        self.register_p.get_email_element().send_keys(email)
    # 输入用户名
    def send_user_name(self,username):
        self.register_p.get_username_element().send_keys(username)
    # 输入密码
    def send_user_password(self,password):
        self.register_p.get_password_element().send_keys(password)
    # 输入验证码
    def send_user_code(self,file_name):
        get_code_text = getcode(self.driver)
        code = get_code_text.code_online(file_name)
        self.register_p.get_code_text_element().send_keys(code)
    #获取文字信息
    def get_user_text(self,info):
        if info =="email_error":
            text=self.register_p.get_email_error_element().text
        elif info =="name_error":
            text=self.register_p.get_name_error_element().text
        elif info =="password_error":
            text=self.register_p.get_password_error_element().text
        else:
            text=self.register_p.get_code_error_element().text
        return text
    #点击注册按钮
    def click_register_button(self):
        self.register_p.get_button_element().click()
    #获取相册按钮文字
    def get_register_text(self):
        return self.register_p.get_button_element().text