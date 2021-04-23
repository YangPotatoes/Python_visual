import requests
import pandas as pd
import time
from random import randint
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

FONT = FontProperties(fname="C:\Windows\Fonts\STXIHEI.TTF")

Header = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/89.0.4389.114 Safari/537.36'}

def CheZhiWang_Spider():
    for i in range(1, 1000):
        print("url准备中")
        url = "http://www.12365auto.com/zlts/0-0-0-0-0-0_0-0-0-0-0-0-0-" + str(i) + ".shtml"
        html_data = requests.get(url=url,headers = Header)
        print("第%d页数据开始爬取" % (i))
        CheZhiWang_data = pd.read_html(html_data.content, encoding="utf-8")
        '''上一条代码用来读取网页的表格数据'''
        print("第%d页数据中..." % (i))
        CheZhiWang_data[0].to_csv("Car_data_G2.csv", mode='a')
        print("第%d页数据爬取完成" % (i))
        print("爬虫伪装中")
        time.sleep(randint(4, 10))
# 1、实现对投诉品牌的分析
car_complain_data = pd.read_csv("CarData.csv", encoding="GBK")
# print(car_complain_data)
# dataframe 去除重复数据drop_duplicates
car_complain_data_drop_duplicate = car_complain_data.drop_duplicates()
# print(car_complain_data_drop_duplicate)
car_brand = car_complain_data_drop_duplicate["投诉车型"]
car_brand_complain_type_and_num = car_brand.value_counts()

car_brand_single = car_brand_complain_type_and_num.keys().tolist()  # 索引
car_brand_single_complain_data = car_brand_complain_type_and_num.tolist()  # 值
'''因为是排序好的数据，可以直接分析'''
# print(car_brand_single[0:10])
# print(car_brand_single_complain_data[0:10])
car_dict = dict(zip(car_brand_single, car_brand_single_complain_data))
'''上面一行代码为创建车品牌与数据直接的映射'''
x = []
y = []
for i in car_dict:
    if car_dict[i] > 20:
        x.append(i)  # 加入品牌
        y.append(car_dict[i])  # 加入品牌对应值

plt.bar(x,y,width=0.3,color = 'r')
plt.xticks(x,FontProperties = FONT)
plt.title("车质网一万条数据分析之\n   投诉最多品牌  \n     by 杨贺昆",FontProperties = FONT)
plt.show()