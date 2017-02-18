import scrapy


class QuotesSpider(scrapy.Spider):
    name = "quotes"
    start_urls = [
        'http://quotes.toscrape.com/page/1/',
        'http://quotes.toscrape.com/page/2/',
    ]

    def parse(self, response):
        page = response.url.split("/")[-2]
        filename = 'quotes-%s.html' % page
        with open(filename, 'wb') as f:
            f.write(response.body)
        self.log('Saved file %s' % filename)

        # Storing the data part
        for quote in response.xpath('//div[contains(@class, "quote")]'):
            yield{
                'text': quote.xpath('span[contains(@class,"text")]/text()').extract_first(),
                'author': quote.xpath('span/small[contains(@class,"author")]/text()').extract_first(),
                'tags': quote.xpath('div/a/text()').extract()
            }
        next_page = response.xpath('//li[contains(@class, "next")]/a/@href').extract_first()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield scrapy.Request(next_page, callback=self.parse)