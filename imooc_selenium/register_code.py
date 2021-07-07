from selenium import webdriver
import time
import  random
from PIL import Image
from util.ShowapiRequest import ShowapiRequest
driver = webdriver.Chrome()
#浏览器初始化
def driver_init(url):
    driver.get(url)
    driver.maximize_window()
    time.sleep(5)
#用户名随机生成
def user_name():
    useremail = ''.join(random.sample('12365487978asdfghjkl',6))
    return useremail
#获取element信息
def get_element(id):
    element = driver.find_element_by_id(id)
    return element
#配置文件读取定位信息
#验证码图片获取
def get_code_image(file_name1,id1,file_name2):
    driver.save_screenshot(file_name1)
    code_element = get_element(id1)
    left = code_element.location["x"]
    top = code_element.location["y"]
    right = code_element.size["width"] + left
    height = code_element.size["height"] + top
    im = Image.open(file_name1)
    img = im.crop((left, top, right, height))
    img.save(file_name2)
#图片识别
def code_online(file_name2):
    r = ShowapiRequest("http://route.showapi.com/1274-2", "675940", "fbf720082ded4bbd83a9767dc8f8741b")
    # r.addBodyPara("imgUrl", "http://pic.4j4j.cn/upload/pic/20130528/a9117a5351.jpg")
    # r.addBodyPara("base64", "")
    r.addFilePara("imgFile", file_name2)
    res = r.post()
    text = res.json()['showapi_res_body']['texts']
    return text
def main():
    driver_init('http://www.5itest.cn/register')
    get_element('register_email').send_keys(user_name()+'163.com')
    get_element('register_nickname').send_keys(user_name())
    get_element('register_password').send_keys(111111)
    get_code_image("D:\\xin\\1.png",'',"D:\\xin\\2.png")
    text = code_online("D:\\xin\\2.png")
    get_element("captcha_code").send_keys(text)
    get_element("register-btn").click()
    driver.close()
main()