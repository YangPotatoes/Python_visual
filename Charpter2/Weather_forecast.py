'''
天气预报小程序 V0.1
'''
import urllib.request
import json
import string
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.font_manager import FontProperties #字体管理器

def Weather_forcast(city,district_code):
    Font = FontProperties(fname="C:\Windows\Fonts\simkai.ttf")

    url = 'http://api.map.baidu.com/weather/v1/?district_id' \
          '='+str(district_code)+'&data_type=all&ak=u49Sd4WWCKnHv8aNwbmAyYl31mw8F18o'
    #print(url)
    url = urllib.parse.quote(url, safe=string.printable)
    page = urllib.request.urlopen(url)
    res = json.loads(page.read())  # json转为dict,json.loads 用于解码 JSON 数据。该函数返回 Python 字段的数据类型
    # print(res["result"]["location"])
    #print(res)

    y_max = []  # 最高温度
    y_min = []  # 最低温度
    x_date = []  # 日期

    for i in res['result']['forecasts']:
        y_max.append(i['high'])
        y_min.append(i['low'])
        x_date.append(i['date'])
    plt.plot(x_date, y_max, color="r", linestyle='--', marker='.')
    plt.plot(x_date, y_min, color='b', linestyle='-.', marker='*')
    # plt.yticks(np.arange(-8,17,4))
    plt.xlabel("日期", FontProperties=Font)
    plt.ylabel("℃")
    plt.title(city + " \n"
                     "uptime:" + str(res['result']['now']['uptime']), FontProperties=Font)
    plt.legend(["max", "min"])
    plt.show()
