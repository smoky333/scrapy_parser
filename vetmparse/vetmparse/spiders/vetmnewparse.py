import scrapy


class VetmnewparseSpider(scrapy.Spider):
    name = "vetmnewparse"
    allowed_domains = ["vetementpro.com"]
    start_urls = ["https://www.vetementpro.com/445-baskets-de-cuisine"]

    def parse(self, response):
        baskets = response.css('div.product-description')

        for basket in baskets:
            yield {
                'title': basket.css('a::text').get(),
                'link': basket.css('a::attr(href)').get(),
                'price': basket.css('span.price::text').get()
            }

