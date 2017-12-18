import scrapy
from scrapy.loader import ItemLoader
from quotesbot.items import Blog

class AdvancedSpider(scrapy.Spider):

    name = "advanced_spider"
    start_urls = [
        'http://blog.csdn.net/',
    ]

    def parse(self, response):
        for quote in response.css("div.blog_list_wrap"):
            itemlodaer = ItemLoader(item=Blog(), response=response)
            itemlodaer.add_value('title', quote.css("h3.csdn-tracking-statistics>a::text").extract_first())
            itemlodaer.add_value('content', quote.css("h3.csdn-tracking-statistics>a::text").extract_first())
            itemlodaer.add_value('tag', quote.css("div.blog_list_b_l>span>a::text").extract_first())
            itemlodaer.add_value('remark', 'nothing to show ')
            blog = itemlodaer.load_item()
            yield blog
        next_page_url = response.css("li.next > a::attr(href)").extract_first()
        if next_page_url is not None:
            yield scrapy.Request(response.urljoin(next_page_url))
