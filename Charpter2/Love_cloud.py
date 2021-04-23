import re
import jieba
import wordcloud
import matplotlib.pyplot as plt
import numpy as np
import PIL.Image as image

def world_cloud(path,lover_nickname,you_nickname,mask_path,word_cloudpath=''):
    f = open(path, encoding='utf-8')
    f_1 = f.readlines()
    for i in f_1:
        if i.find(you_nickname) > 1:
            f_1.remove(i)
        if i.find(lover_nickname) > 1:
            f_1.remove(i)
    strf = ' '.join(f_1)
    list1 = re.findall(r'/.{2,3}', strf)
    list2 = re.findall(r'\[.+?\]', strf)
    set1 = set(list1)
    set2 = set(list2)
    for item in set1:
        strf = strf.replace(item, '')
    for item in set2:
        strf = strf.replace(item, '')
    strf = strf.replace('请使用最新版本手机QQ查看', '')
    strf = strf.replace('请使用最新版手机QQ体验新功能', '')
    strf = strf.replace('对方已成功接收了您发送的离线文件', '')
    strf = strf.replace('嗯嗯', '')
    strf.replace('\n', '')

    word_list = jieba.cut(strf, cut_all=True)
    word = ' '.join(word_list)
    mask = np.array(image.open(mask_path))
    wordcloud1 = wordcloud.WordCloud(
        mask=mask,
        background_color='#FFFFFF',
        # 若想生成中文字体,需添加中文字体路径
        font_path="Alibaba-PuHuiTi-Heavy.otf"
    ).generate(word)
    # 返回对象
    image_produce = wordcloud1.to_image()
    # 保存图片
    wordcloud1.to_file(word_cloudpath)
    # 显示图像
    image_produce.show()
