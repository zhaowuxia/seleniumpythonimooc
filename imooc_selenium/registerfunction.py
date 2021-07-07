from selenium import webdriver
import time
import  random
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
from base.find_element import FindElement
from readini import readini
read =readini()
class registerfunction(object,):
    def __init__(self,url,i):
        self.driver = self.get_driver(url,i)
    def get_driver(self,url,i):
        if i == 1:
            driver = webdriver.Chrome()
        elif i ==2:
            driver = webdriver.Ie()
        else:
            driver = webdriver.Firefox()
        driver.get(url)
        driver.maximize_window()
        return driver

    # 输入用户信息
    def send_user_info(self, key, data):
        self.get_user_element(key).send_keys(data)

    # 定位用户信息，获取element
    def get_user_element(self, key):
        find_element = FindElement(self.driver)
        user_element = find_element.get_element(key)
        return user_element
#输入用户信息
    '''
    
    def send_user_info(self,node,key,value):
        findelement = FindElement(self.driver)
        element = findelement.get_element(node,key)
        element.send_key(value)
        '''
#获取随机数
    def user_name(self):
        useremail = ''.join(random.sample('12365487978asdfghjkl',6))
        return useremail
#验证码图片获取
    def get_code_image(self,file_name1,key,file_name2):
        self.driver.save_screenshot(file_name1)
        findelement = FindElement(self.driver)
        code_element =findelement.get_element(key)
        left = code_element.location["x"]
        top = code_element.location["y"]
        right = code_element.size["width"] + left
        height = code_element.size["height"] + top
        im = Image.open(file_name1)
        img = im.crop((left, top, right, height))
        img.save(file_name2)
#图片识别
    def code_online(self,file_name2):
        r = ShowapiRequest("http://route.showapi.com/1274-2", "675940", "fbf720082ded4bbd83a9767dc8f8741b")
        # r.addBodyPara("imgUrl", "http://pic.4j4j.cn/upload/pic/20130528/a9117a5351.jpg")
        # r.addBodyPara("base64", "")
        r.addFilePara("imgFile", file_name2)
        res = r.post()
        text = res.json()['showapi_res_body']['texts']
        return text
    def main(self):
        read.load_ini("D:/python/Tools/config/localelement.ini")
        findelement = FindElement(self.driver)
        user_name_info=self.user_name()
        user_email=user_name_info+'163.com'
        self.get_code_image("D:\\xin\\3.png",'getcode','D:\\xin\\4.png')
        code_text = self.code_online('D:\\xin\\4.png')
        self.send_user_info('useremail',user_email)
        self.send_user_info('username', user_name_info)
        self.send_user_info('password', '111111')
        self.send_user_info('code', code_text)
        self.get_user_element('register').click()
        code_error = self.get_user_element("code_text_error")
        if code_error==None:
            print("注册成功")
        else:
            self.driver.save_screenshot("D:\\xin\\error.png")
        time.sleep(5)
        self.driver.close()
if __name__ == '__main__':
    for i in range(3):
        re = registerfunction('http://www.5itest.cn/register',i)
        re.main()






