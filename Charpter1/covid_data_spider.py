#!/usr/bin/python3.9
# -*- coding: utf-8 -*-
#
# Copyright (C) 2021 #
# @Time    : 2021/4/15 22:29
# @Author  : YangZi
# @Email   : 1014191945@qq.com
# @File    : covid_data_spider.py
# @Software: PyCharm
# for:
import requests
import json
import time
import datetime
import matplotlib.pyplot as plt
import numpy as np

url = 'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5&callback=&_=%d'%int(time.time()*1000)
data = json.loads(requests.get(url=url).json()['data'])
num = data['areaTree'][0]['children']

# 解析确诊数据
total_data = {}
for item in num:
    if item['name'] not in total_data:
        total_data.update({item['name']:0})
    for city_data in item['children']:
        total_data[item['name']] +=int(city_data['total']['confirm'])

# 解析疑似数据
total_suspect_data = {}
for item in num:
    if item['name'] not in total_suspect_data:
        total_suspect_data.update({item['name']:0})
    for city_data in item['children']:
        total_suspect_data[item['name']] +=int(city_data['total']['suspect'])


# 解析死亡数据
total_dead_data = {}
for item in num:
    if item['name'] not in total_dead_data:
        total_dead_data.update({item['name']:0})
    for city_data in item['children']:
        total_dead_data[item['name']] +=int(city_data['total']['dead'])

# 解析治愈数据
total_heal_data = {}
for item in num:
    if item['name'] not in total_heal_data:
        total_heal_data.update({item['name']:0})
    for city_data in item['children']:
        total_heal_data[item['name']] +=int(city_data['total']['heal'])

# 解析新增确诊数据
total_new_data = {}
for item in num:
    if item['name'] not in total_new_data:
        total_new_data.update({item['name']:0})
    for city_data in item['children']:
        total_new_data[item['name']] +=int(city_data['today']['confirm'])


#统计数据并输出
names = list(total_data.keys())
num1 = list(total_data.values())
num2 = list(total_suspect_data.values())
num3 = list(total_dead_data.values())
num4 = list(total_heal_data.values())
num5 = list(total_new_data.values())


today=datetime.date.today()
f=open('./疫情-%s.csv'%(today),'w',encoding='utf-8')
f.write('省份,确诊人数,死亡人数,治愈人数,新增确诊\n')
i = 0
while i<len(names):
    f.write(names[i]+','+str(num1[i])+','+str(num3[i])+','+str(num4[i])+','+str(num5[i])+'\n')
    i = i + 1




# #绘制柱形图
#
# plt.figure(figsize=[100,60])
# plt.rcParams['font.sans-serif'] = ['SimHei']
# plt.rcParams['axes.unicode_minus'] = False
#
# #绘制确诊数据
# p1 = plt.subplot(221)
# names = total_data.keys()
# nums = total_data.values()
# print(names)
# print(nums)
# print(total_data)
# plt.bar(names, nums, width=0.5, color='green')
# plt.ylabel("确诊人数", rotation=90,size=50)
# plt.xticks(list(names), rotation=-60, size=50)
# for a, b in zip(list(names), list(nums)):
#     plt.text(a, b, b, ha='center', va='bottom', size=35)
# plt.sca(p1)
#
# #绘制新增确诊数据
# p2 = plt.subplot(222)
# names = total_new_data.keys()
# nums = total_new_data.values()
# print(names)
# print(nums)
# plt.bar(names, nums, width=0.5, color='yellow')
# plt.ylabel("新增确诊人数", rotation=90,size=50)
# plt.xticks(list(names), rotation=-60, size=50)
# for a, b in zip(list(names), list(nums)):
#     plt.text(a, b, b, ha='center', va='bottom', size=35)
# plt.sca(p2)
#
# #绘制死亡数据
# p3 = plt.subplot(223)
# names = total_dead_data.keys()
# nums = total_dead_data.values()
# print(names)
# print(nums)
# plt.bar(names, nums, width=0.5, color='blue')
# plt.xlabel("地区")
# plt.ylabel("死亡人数", rotation=90,size=50)
# plt.xticks(list(names), rotation=-60, size=50)
# for a, b in zip(list(names), list(nums)):
#     plt.text(a, b, b, ha='center', va='bottom', size=35)
# plt.sca(p3)
#
# #绘制治愈数据
# p4 = plt.subplot(224)
# names = total_heal_data.keys()
# nums = total_heal_data.values()
# print(names)
# print(nums)
# plt.bar(names, nums, width=0.3, color='red')
# plt.xlabel("地区")
# plt.ylabel("治愈人数", rotation=90,size=50)
# plt.xticks(list(names), rotation=-60, size=50)
# for a, b in zip(list(names), list(nums)):
#     plt.text(a, b, b, ha='center', va='bottom', size=35)
# plt.sca(p4)
# plt.show()
