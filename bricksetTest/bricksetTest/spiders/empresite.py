# -*- coding: utf-8 -*-
from scrapy.spiders import CrawlSpider, Rule
from scrapy.linkextractors import LinkExtractor



class EmpresiteSpider(CrawlSpider):
    name = 'empresite'
    allowed_domains = ['www.empresite.eleconomista.es/']
    start_urls = ['https://empresite.eleconomista.es/Actividad/EMPRESAS-TECNOLOGICAS/']

    rules = (
        Rule(LinkExtractor(allow=(), restrict_css=('.pagination01',)),
             callback="parse_item",
             follow=True),)

    def parse_item(self, response):
        print('Processing..' + response.url)
