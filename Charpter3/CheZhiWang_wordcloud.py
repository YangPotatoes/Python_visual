import pandas as pd
import wordcloud # 词云库
import numpy as np
import PIL.Image as image
import jieba

# 读取数据
car_data = pd.read_csv("CarData.csv",encoding="GBK")

# 数据预处理
car_data_drop_dup = car_data.drop_duplicates() #去重
# 获取需求数据
word = ''
for complain in car_data_drop_dup["典型问题4"].dropna():
    word = word + complain +' '
for complain in car_data_drop_dup["典型问题"].dropna():
    word = word + complain +' '
for complain in car_data_drop_dup["典型问题2"].dropna():
    word = word + complain +' '
# word = ''
# for ask in car_data_drop_dup["问题简述"]:
#     print(ask)

# word = ''''''

# word_list = jieba.cut(word,cut_all="true") # 将文章分词
# word = ' '.join(word_list)

# mask = np.array(image.open("I_LOVE_YOU.png"))

wordcloud1 = wordcloud.WordCloud(
    font_path="C:\Windows\Fonts\STCAIYUN.TTF",
    background_color = "#FFFFFF",
    width=1920,
    height=1080,
    max_font_size=50
    # mask=mask
).generate(word)
image_produce = wordcloud1.to_image()
image_produce.show()
