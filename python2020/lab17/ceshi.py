# ceshi
# coding=utf-8

from wordcloud import WordCloud
import wordcloud
from imageio import imread
import matplotlib.pyplot as pyl
import numpy
from os import path
a=imread('photo.jpg')
mark=a
b=open('poem2.txt', 'r', encoding='utf-8')
c=b.read()
imageword = WordCloud(background_color='white',width=1920, height=1080, max_words=800, max_font_size=500, mask=mark,font_path = 'C://Windows//Fonts//simfang.ttf')
imageword.generate_from_text(c)
imageword.to_file('WORDCLOUD.png')
pyl.imshow(imageword)
pyl.axis('off')
pyl.show()
b.close()
