# -*- coding: utf-8 -*-
from logging import exception

import scrapy
from time import sleep
import scrapy
from bs4 import BeautifulSoup
from scrapy import Spider,Request
import json

from tc58.items import CourseItem


class ChuzuSpider(scrapy.Spider):
    name = 'chuzu'
    allowed_domains = ['wh.58.com']
    start_urls = ['http://wh.58.com/chuzu/pn1/']


    # def start_requests(self):
    #     # yield Request(self.start_urls,callback=self.detail_parse)
    #     yield Request(self.start_urls,callback=self.parse())


    # def detail_parse(self,response):
    #
    #
    #

    def parse(self, response):
        item = CourseItem()
        for box in response.xpath('//ul[@class="listUl"]/li'):

            item['link'] = box.css('div.des > h2 > a::attr("href")').extract()
            try:
                item['link'] = item['link'][0].strip()
            except IndexError:
                item['link'] = ''


            item['title'] = box.xpath('.//div[@class="des"]/h2/a/text()').extract()
            try:
                item['title'] = item['title'][0].strip()
            except IndexError:
                item['title'] = ''
            item['number'] = box.xpath('.//div[@class="listliright"]/div[@class="money"]/b/text()').extract()
            try:
                item['number'] = item['number'][0]
            except IndexError:
                item['number'] = ''
            item['area'] = box.xpath('.//div[@class="des"]/p[@class="add"]/a/text()').extract()
            try:
                item['area'] = item['area']
            except IndexError:
                item['area'] = ''
            item['huxing'] = box.xpath('.//div[@class="des"]/p[@class="room"]/text()').extract()
            try:
                item['huxing'] = item['huxing'][0]
            except IndexError:
                item['huxing'] = ''
            item['nature'] = box.xpath('.//div[@class="des"]/div[@class="jjr"]/text()').extract()
            try:
                item['nature'] = item['nature'][0].strip()
            except IndexError:
                item['nature'] = ''

            yield item

            next_page = response.xpath(
                './/li[@id="bottom_ad_li"]/div[@class="pager"]/a[@class="next"]/@href').extract_first()

            if next_page:
                next_page = response.urljoin(str(next_page))

                yield scrapy.Request(next_page, callback=self.parse)
            else:
                print(None)



