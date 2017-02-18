import scrapy


class GardenaSpider(scrapy.Spider):
    name = "gardena"
    start_urls = [
        'https://www.bricoetloisirs.ch/magasins/gardena',
    ]

    def parse(self, response):
        for page in range(1, 30):
            url = 'https://www.bricoetloisirs.ch/coop/ajax/nextPage/(cpgnum=1&layout=7.01-14_181_69_164_183&uiarea=2&carea=%24ROOT&fwrd=frwd0&cpgsize=12)/.do?page=' + str(page) + '&_=1487226307696'
            yield scrapy.Request(url)
            # with open('gardena' + str(page) + '.html', 'wb') as f:
            #     f.write(response.body)
            self.log('SUCCESS')
