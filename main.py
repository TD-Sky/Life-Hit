import os

# 资源文件
CHATS = os.path.join("assets", "data", "bili.json")
IMAGES = os.path.join("cache", "images")

if __name__ == '__main__':
    """
    想要启动爬虫，必须不存在数据存储文件和词云图
    两者之一存在，爬虫都不会执行
    """
    os.makedirs(IMAGES, exist_ok=True)
    if not os.path.exists(CHATS) and not os.listdir(IMAGES):
        os.system("scrapy crawl life_hit")

