import pandas as pd
import Charpter2.Weather_forecast as CW
#  xlrd

weather_district_id = pd.read_excel("weather_district_id.xlsx")
city = input("请输入你要查询的区县:")
index = 0
for cityi in weather_district_id['district']: # 遍历城市，寻找所在行索引
    index = index+1
    if cityi == city:
        print("找到了"+cityi)
        break
index1 = index
districtcode_id = 0
# 根据行索引，找到district_id
for districtcodei in weather_district_id['districtcode']:
    index1 = index1 - 1
    if index1 == 0:
        districtcode_id = districtcodei
        break
print(districtcodei)
CW.weather_forest(city,district_id=districtcodei) # 调用函数