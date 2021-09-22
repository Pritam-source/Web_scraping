import scrapy


class WikiSpider(scrapy.Spider):
    name = 'wiki'
    
    start_urls = ['https://en.wikipedia.org/wiki/Eiffel_Tower']

    def parse(self, response):
        raw_image_urls=response.css('.image  :: atr(src)').getall()
        print(raw_image_urls)

        # clean_image_urls =[]
        # for img_url in raw_image_urls:
        #     print(img_url)
        #     clean_image_urls.append(response.urljoin(img_url))


        # yield {
        #     'image_urls': clean_image_urls
        # }
        
