import scrapy 

class Quotespider (scrapy.Spider):
    name= 'quotes'
    url= ['http://quotes.toscrape.com/']

    def parse(self, response):
        title= response.css('title::text').extract()
        yield { 'titletext': title }