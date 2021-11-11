# 17.2
# coding=utf-8
from wordcloud import WordCloud
import wordcloud
from imageio import imread
import matplotlib.pyplot as pyl
import numpy
from os import path
#ziti = wordcloud.font_path('C://Windows//Fonts//simfang.ttf')
Asuka = imread('Mikoto3.png')
mark = Asuka
Assuses = open('Assus.txt', 'r', encoding='utf-8')
Assus = Assuses.read()
imageword = WordCloud(background_color='white', width=1920, height=1080, max_words=800, max_font_size=500, mask=mark,
          font_path = 'C://Windows//Fonts//simfang.ttf')
imageword.generate_from_text(Assus)

imageword.to_file('WORDCLOUD.png')
pyl.imshow(imageword)
pyl.axis('off')
pyl.show()
Assuses.close()



