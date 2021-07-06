#用来执行操作
from handle.register_handle import registerhandle
class registerbusiness(object):
    def __init__(self,driver):
        self.register_h=registerhandle(driver)
    def user_base(self,email,name,password,code):
        self.register_h.send_user_email(email)
        self.register_h.send_user_name(name)
        self.register_h.send_user_password(password)
        self.register_h.send_user_code(code)
        self.register_h.click_register_button()
        self.register_h.get_register_text()
    def register_success(self):
        if self.register_h.get_register_text()== None:
            return True
        else:
            return False
    #执行操作
    def login_email_error(self,email,name,password,code):
        self.user_base(email,name,password,code)
        if self.register_h.get_user_text('email_error')==None:
            print("邮箱检验不成功")
            return True
        else:
            return False
    def regiser_function(self,email,username,password,file_name,assertcode):
        self.user_base(email, username, password, file_name)
        if self.register_h.get_user_text(assertcode) == None:
            print("邮箱检验不成功")
            return True
        else:
            return False
    #用户名错误
    def login_name_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('username_error')==None:
            print("用户名检验不成功")
            return True
        else:
            return False
    #密码错误
    def password_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('password_error') == None:
            print("密码检验不成功")
            return True
        else:
            return False
    #验证码错误
    def code_error(self, email, name, password, code):
        self.user_base(email, name, password, code)
        if self.register_h.get_user_text('code_error') == None:
            print("验证码检验不成功")
            return True
        else:
            return False

