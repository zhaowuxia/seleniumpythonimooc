from PIL import Image
from util.ShowapiRequest import ShowapiRequest
import time
class getcode:
    def __init__(self,driver):
        self.driver = driver
    # 验证码图片获取
    def get_code_image(self,file_name):
        self.driver.save_screenshot(file_name)
        code_element = self.driver.find_element_by_id('getcode_num')
        left = code_element.location["x"]
        top = code_element.location["y"]
        right = code_element.size["width"] + left
        height = code_element.size["height"] + top
        im = Image.open(file_name)
        img = im.crop((left, top, right, height))
        img.save(file_name)
        time.sleep(1)

    # 图片识别
    def code_online(self,file_name1):
        self.get_code_image(file_name1)
        r = ShowapiRequest("http://route.showapi.com/1274-2", "675940", "fbf720082ded4bbd83a9767dc8f8741b")
        # r.addBodyPara("imgUrl", "http://pic.4j4j.cn/upload/pic/20130528/a9117a5351.jpg")
        # r.addBodyPara("base64", "")
        r.addFilePara("imgFile", file_name1)
        res = r.post()
        time.sleep(1)
        text = res.json()['showapi_res_body']['texts']
        return text