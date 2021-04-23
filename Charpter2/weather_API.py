'''
天气预报小程序 V0.1
'''
import urllib
import requests
import json
import string
import matplotlib.pyplot as plt

key = 'u49Sd4WWCKnHv8aNwbmAyYl31mw8F18o'
url = "https://wis.qq.com/weather/common"
querystring = {"source":"pc","weather_type":"forecast_1h|forecast_24h|index|alarm|limit|tips","province":"陕西","city":"西安","county":"长安"}
response = requests.request(method='Get',url=url,params=querystring)  # 打开URL
res = json.loads(response.text)  # json转为dict,json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
print(res['data']['forecast_24h'])