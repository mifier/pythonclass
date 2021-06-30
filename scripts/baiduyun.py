# encoding:utf-8

import requests
import base64


# client_id 为官网获取的AK， client_secret 为官网获取的SK
#host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=mtdG6mVRCAgrH5HrzEGlzkFn&client_secret=Ah3lumhhRSihKjpC3AYWHgkjjQa7732A'
#host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=uhpGFeEfj5MPhDGwjHhkfSEr&client_secret=FyyGVwYvk3kD6uTme3uLYAiTLRwFPDIQ'
#host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=6a51qGaEPqdT1jX7987eST6A&client_secret=3dGToiH4uY3EtiyoiOa1niXKhfEdvMHM'
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=7go3MmP1OIEGk32x3eyFGAKH&client_secret=WAoxyqDmtgQnCXGN3HPM24D97cXOmTF3'
# host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=ZubDwZ4mz7XRPefymLPRK1ty&client_secret=mwPDrghfvfWaxO2ktOLGrPzTeaKGLPnt'
host = 'https://aip.baidubce.com/oauth/2.0/token?grant_type=client_credentials&client_id=Bg6kPuNRBfqfANrlHPDGv5Ay&client_secret=PbsDbSFNkLPG1YqGMH48NwhNrNYd9ZYr'

response = requests.get(host)
if response:
    print(response.json())


# # 图像识别组合API

# request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/animal"
# # 二进制方式打开图片文件
# f = open("G:\\工具\\图片\\23.jpg", 'rb')
# img = base64.b64encode(f.read())
# params = {"image": img}
# access_token = '24.e5ebfd5bfd68746ef005899172c950e5.2592000.1621995651.282335-24060223'
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print(response.json())

# # 人脸识别
# request_url = "https://aip.baidubce.com/rest/2.0/face/v3/detect"
# f = open("C:\\Users\\sfreqwre\\Desktop\\test\\38.jpg", 'rb')
# img = base64.b64encode(f.read())
# params = "{\"image\":\"" +str(img, encoding="utf-8")+ "\",\"image_type\":\"BASE64\",\"face_field\":\"faceshape,facetype\"}"
# access_token = '24.f7c625fbe924e4487471daa45c97d5fb.2592000.1621997449.282335-24066525'
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/json'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print(response.json())

# #人体关键点识别
# request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/body_analysis"
# # 二进制方式打开图片文件
# f = open("C:\\Users\\sfreqwre\\Desktop\\test\\38.jpg", 'rb')
# img = base64.b64encode(f.read())
# params = {"image":img}
# access_token = '24.67a521067178c82499606b11edace371.2592000.1621999444.282335-24067015'
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print (response.json())


# # 文本审核接口
# request_url = "https://aip.baidubce.com/rest/2.0/solution/v1/text_censor/v2/user_defined"

# params = {"text":"不要侮辱伟大的乐侃"}
# access_token = '24.91196d6c2fd0d67b3b238465b81eee31.2592000.1621999753.282335-24067107'
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print (response.json())


# # 相似图检索—检索

# request_url = "https://aip.baidubce.com/rest/2.0/image-classify/v1/realtime_search/similar/search"
# # 二进制方式打开图片文件
# f = open("C:\\Users\\sfreqwre\\Desktop\\test\\5.jpg", 'rb')
# img = base64.b64encode(f.read())

# params = {"image": img, "pn": 200, "rn": 100}
# access_token = '24.001f88a4ae7178622f00a50640f8c0bd.2592000.1622000242.282335-24067167'
# request_url = request_url + "?access_token=" + access_token
# headers = {'content-type': 'application/x-www-form-urlencoded'}
# response = requests.post(request_url, data=params, headers=headers)
# if response:
#     print(response.json())


# 图像去雾


request_url = "https://aip.baidubce.com/rest/2.0/image-process/v1/dehaze"
# 二进制方式打开图片文件
f = open("C:\\Users\\sfreqwre\\Desktop\\test\\5.jpg", 'rb')
img = base64.b64encode(f.read())

params = {"image":img}
access_token = '24.0252bb6913cfeaf9795c3e2a3f224466.2592000.1622016096.282335-24069495'
request_url = request_url + "?access_token=" + access_token
headers = {'content-type': 'application/x-www-form-urlencoded'}
response = requests.post(request_url, data=params, headers=headers)
if response:
    print (response.json())


