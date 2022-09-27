
import scrapy
class QuoteSpider(scrapy.Spider):
    name = 'quotes'
    start_urls = ["https://quotes.toscrape.com/"]
    def parse(self, response):
        all_div_quotes = response.css('div.quote')
        for quota in all_div_quotes:
            title = quota.css('span.text::text').extract()
            author = quota.css('.author::text').extract()
            tag = quota.css(".tag::text").extract()
            yield {'title' : title,
                    'author' : author,
                    'tag' : tag }