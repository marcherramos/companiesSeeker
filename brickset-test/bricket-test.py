import scrapy

class BricketSpider(scrapy.Spider):
    name="Bricket Spider"
    start_Urls=["https://brickset.com/sets/year-2016"]