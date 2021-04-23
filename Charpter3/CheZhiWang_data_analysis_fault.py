import numpy as np
import pandas as pd
import wordcloud
import PIL.Image as image


car_Data = pd.read_csv("CarData.csv",encoding="GBK")# 读取数据

typical_fault = []
word =''
for fault in car_Data["典型问题2"].dropna(): #去除空值
    typical_fault.append(fault)
    word = word+fault+' '
print(word)

mask = np.array(image.open("logo.png"))

wordcloud1 = wordcloud.WordCloud(
    font_path="C:\Windows\Fonts\simkai.ttf",
    background_color='#FFFFFF',
    mask=mask
).generate(word)
image_produce = wordcloud1.to_image()
# 保存图片
#wordcloud1.to_file(word_cloudpath)
# 显示图像
image_produce.show()
