# coding:utf-8
import jieba  # 分词
import matplotlib.pyplot as plt  # 数据可视化
from wordcloud import WordCloud, ImageColorGenerator, STOPWORDS  # 词云
import numpy as np  # 科学计算
from PIL import Image  # 处理图片
import imageio
import collections


def stopwordslist(filepath):
    stopwords = [line.strip() for line in open(filepath, 'r', encoding='utf-8').readlines()]
    return stopwords


def draw_cloud(text, graph, save_name):
    textfile = open(text).read()  # 读取文本内容
    jieba.load_userdict('user_dict.txt')
    wordlist = jieba.cut(textfile, cut_all=False)  # 中文分词

    space_list = " ".join(wordlist)  # 连接词语
    backgroud = np.array(Image.open(graph))  # 背景轮廓图
    mywordcloud = WordCloud(background_color="white",  # 背景颜色
                            mask=backgroud,  # 写字用的背景图，从背景图取颜色
                            max_words=100,  # 最大词语数量
                            stopwords=stopwords,  # 停用词
                            font_path="C:/Windows/Fonts/STZHONGS.ttf",  # 字体
                            min_font_size=10,
                            # max_font_size=200,  # 最大字体尺寸
                            random_state=50,  # 随机角度
                            scale=2,  # 默认值1。值越大，图像密度越大
                            collocations=False,  # 避免重复单词
                            )

    mywordcloud = mywordcloud.generate(space_list)  # 生成词云

    ImageColorGenerator(backgroud)  # 生成词云的颜色

    plt.imshow(mywordcloud)  # 显示词云

    '''mk = imageio.imread("horse.jpg")
    image_colors = ImageColorGenerator(mk)
    plt.imshow(mywordcloud.recolor(color_func=image_colors), interpolation="bilinear")  # 按蒙板颜色显示词云'''

    plt.axis("off")
    plt.show()


if __name__ == '__main__':
    stopwords = set()
    stopwords.update(stopwordslist('stopwords/cn_stopwords.txt'))
    stopwords.update(stopwordslist('stopwords/hit_stopwords.txt'))
    stopwords.update(stopwordslist('stopwords/baidu_stopwords.txt'))
    stopwords.update(stopwordslist('stopwords/scu_stopwords.txt'))
    stopwords.update(["然而", "这样", "另一方面", "但是", "因此", "我们", "一个", "如果",
                      '它们', '具有', '人们', '可以', '这个', '这种', '不能', '因为',
                      '或者', '没有', '这些', '一种', '非常', '可能', '他们', '而且',
                      '所有', '也许', '就是', '认为', '正如', '必须', '确定', '所以',
                      '任何', '发生', '甚至', '能够', '过去', '对于', '知道', '这是',
                      '现在', '不同', '并且', '似乎', '那样', '其他', '什么', '不是',
                      '那么', '一点', '已经', '之间', '如何', '仍然'])
    draw_cloud(text="cloud_txt/覆汉.txt", graph="cloud_image/horse.jpg", save_name='覆汉词云.png')
