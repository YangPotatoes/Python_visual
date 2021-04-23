import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.font_manager import FontProperties

car_Data = pd.read_csv("CarData.csv",encoding="GBK")# 读取数据
car_Data = car_Data.drop_duplicates() # 去重

# 变量名要有意义！！
car_Data_type_complain_data = car_Data["投诉品牌"].value_counts()
# print(car_Data_type_complain_data)

car_type = car_Data_type_complain_data.keys().tolist() #x轴
complain_data = car_Data_type_complain_data.values.tolist()#y轴
car_dict = dict(zip(car_type,complain_data)) #做出字典映射
x = []
y = []
for complain_type in car_dict:
    if car_dict[complain_type]>200:
        y.append(car_dict[complain_type])
        x.append(complain_type)
print(x)
Font = FontProperties(fname="C:\Windows\Fonts\msyh.ttc")  # 字体
plt.bar(x,y,width=0.4,color='r')
plt.xticks(x, FontProperties = Font)
plt.title("车质网一万条数据分析\n——投诉最多车系、\n---------------------by 杨贺昆",
          fontsize=20,FontProperties=Font)
plt.show()