import scrapy
from scrapy.loader import ItemLoader
from quotesbot.items import Blog


class juniorSpider(scrapy.Spider):
    name = "junior_spider"
    start_urls = [
        'http://blog.csdn.net/',
    ]

    def parse(self, response):
        for quote in response.css("div.blog_list_wrap"):
            for quote in response.css("div.blog_list_wrap"):
                print('hello bitch')
                yield {
                    'title': quote.css("h3.csdn-tracking-statistics>a::text").extract_first(),
                    'content': quote.css("h3.csdn-tracking-statistics>a::text").extract_first(),
                    'tags': quote.css("div.blog_list_b_l>span>a::text").extract_first()
                }
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))