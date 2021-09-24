import scrapy
from scrapy_selenium import SeleniumRequest
from ..items import QuotesItem

class QSpider(scrapy.Spider):
    name = 'q'
    url = 'https://quotes.toscrape.com'
    allowed_domains = ['quotes.toscrape.com/']

    def start_requests(self):
        yield SeleniumRequest(url='https://quotes.toscrape.com', callback=self.parse)

    def parse(self, response):
        items =QuotesItem()
        for element in response.selector.xpath('//div[@class="quote"]'):
            text = element.xpath('./span/text()').extract_first()
            author = element.xpath('.//small[@class="author"]/text()').extract_first()
            items['author']=author
            items['text']=text
            yield items
        next_page=response.css('li.next a::attr(href)').get()
        if next_page is not None:
            full_url='https://quotes.toscrape.com'+next_page
            print("website:",full_url)
            start_requests()

