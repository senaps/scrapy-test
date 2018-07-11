# -*- coding: utf-8 -*-
import scrapy
from ..items import ReditItem

class FlaskSpider(scrapy.Spider):
    name = 'flask'
    allowed_domains = ['https://www.reddit.com/r/flask/']

    start_urls = ['https://www.reddit.com/r/flask/']

    def parse(self, response):
        links = []
        for link in response.css('div.scrollerItem'):
            title = link.css('h2.xfe0h7-0::text').extract_first()
            count = link.css('div._1rZYMD_4xY3gRcSS3p8ODO::text').extract_first()
            redit_item = ReditItem(title=title, count=count)
            yield redit_item
