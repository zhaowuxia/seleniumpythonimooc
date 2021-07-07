from base.find_element import FindElement
class registerpage(object):
    def __init__(self,driver):
        self.fd=FindElement(driver)
    #获取邮箱元素
    def get_email_element(self):
        return self.fd.get_element('useremail')
    # 获取用户名元素
    def get_username_element(self):
        return self.fd.get_element('username')
    # 获取密码元素
    def get_password_element(self):
        return self.fd.get_element('password')
    #获取验证码元素
    def get_code_text_element(self):
        return self.fd.get_element('code_text')
    # 获取注册按钮元素
    def get_button_element(self):
        return self.fd.get_element('button')
    # 获取邮箱错误元素
    def get_email_error_element(self):
        return self.fd.get_element("useremail_error")
    # 获取用户名错误元素
    def get_name_error_element(self):
        return self.fd.get_element("username_error")
    # 获取密码错误元素
    def get_password_error_element(self):
        return self.fd.get_element("password_error")
    # 获取验证码错误元素
    def get_code_error_element(self):
        return self.fd.get_element("code_error")

