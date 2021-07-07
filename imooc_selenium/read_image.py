#image = Image.open("D:\\xin\\imooc1.png")
#text = pytesseract.image_to_string(image)#只能识别规则的验证码图片
#print(text)
from util.ShowapiRequest import ShowapiRequest
r = ShowapiRequest("http://route.showapi.com/1274-2","675940","fbf720082ded4bbd83a9767dc8f8741b" )
#r.addBodyPara("imgUrl", "http://pic.4j4j.cn/upload/pic/20130528/a9117a5351.jpg")
#r.addBodyPara("base64", "")
r.addFilePara("imgFile", "D:\\xin\\a9.jpg")
res = r.post()
text=res.json()['showapi_res_body']['texts']
print(text) # 返回信息