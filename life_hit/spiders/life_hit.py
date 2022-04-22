from scrapy import Spider, Request

class LifeHit(Spider):
    name = "life_hit"
    start_urls = ["https://api.bilibili.com/x/web-interface/ranking/region?rid=160"]


    def parse(self, response):
        ranking = response.json()

        self.logger.info("Successfully got rank list")

        for item in ranking["data"][:10]:
            bvid: str = item["bvid"]

            request = \
                response.follow(f'https://api.bilibili.com/x/player/pagelist?bvid={bvid}',
                                callback=self.parse_video)
            request.cb_kwargs["title"] = item["title"]
            request.cb_kwargs["url"] = f'https://www.bilibili.com/{bvid}'

            yield request


    def parse_video(self, response, title, url):
        video = response.json()

        cid: int = video["data"][0]["cid"]

        self.logger.info(f"Successfully got cid: {cid}")

        request = response.follow(f"https://api.bilibili.com/x/v1/dm/list.so?oid={cid}",
                                  callback=self.parse_chats)
        request.cb_kwargs["title"] = title
        request.cb_kwargs["url"] = url

        yield request


    def parse_chats(self, response, title, url):
        self.logger.info(f"Successfully got chats of {title}")

        yield {
            "title": title,
            "url": url,
            "chats": response.xpath(r'//d/text()').extract(),
        }

