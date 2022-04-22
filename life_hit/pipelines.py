# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
import jieba
import os.path
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
from wordcloud import WordCloud


# 资源文件
STOP = os.path.join("assets", "template", "stop.txt")
RESERVE = os.path.join("assets", "template", "reserve.txt")
BG = os.path.join("assets", "template", "rank.png")
FONT = os.path.join("assets", "fonts", "NotoSansCJKsc-Regular.otf")


class LifeHitPipeline:

    def open_spider(self, spider):
        """准备停用词，保留词，背景图"""
        with open(STOP, encoding="utf-8") as fp:
            self.stop_words = fp.read().splitlines()

        with Image.open(BG) as img:
            self.mask = np.array(img)

        jieba.load_userdict(RESERVE)


    def process_item(self, item, spider):
        adapter = ItemAdapter(item)
        jb = jieba.cut(''.join(adapter["chats"]))
        bullet_chat = ' '.join([word for word in jb if len(frozenset(word)) > 1])

        wordcloud = WordCloud(font_path=FONT,
                                mask=self.mask,
                                background_color='white',
                                stopwords=self.stop_words,
                                max_words=100,
                                scale=5,
                                contour_width=3,
                                contour_color="white")\
                    .generate(bullet_chat)

        plt.axis("off")

        pic = os.path.join("cache", "images", f'{adapter["title"]}.jpg')
        wordcloud.to_file(pic)

        return item

