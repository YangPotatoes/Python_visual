'''
遇到问题没人解答？小编创建了一个Python学习交流QQ群：531509025
寻找有志同道合的小伙伴，互帮互助,群里还有不错的视频学习教程和PDF电子书！
'''
from PIL import Image


def transparence_white(img):
    sp = img.size
    width = sp[0]
    height = sp[1]
    for yh in range(height):
        for xw in range(width):
            dot = (xw, yh)
            color_d = img.getpixel(dot)  # 与cv2不同的是，这里需要用getpixel方法来获取维度数据
            if (color_d[3] == 0):
                color_d = (255, 255, 255, 255)
                img.putpixel(dot, color_d)  # 赋值的方法是通过putpixel
    return img

img = Image.open('caixukun1.jpg')
img = transparence_white(img)
# img.show()  # 显示图片
img.save('caixunkun1_Gai.jpg')  # 保存图片
