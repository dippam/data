import scrapy

class EppiSpider(scrapy.Spider):
    name = 'eppi'
    start_urls = ['http://www.dippam.ac.uk/eppi/']

    # Go the index, and fetch a list of result links
    def parse(self, response):
        for href in response.css('.list .result h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_document)

    # Snarf the dd elements from the metadata list.
    # Pages is stored in the pagination section of the #toolbar.
    def parse_document(self, response):
        yield {
            'title': response.css('h1.title').extract()[0],
            'source': response.css('#metadata dl dd[0]').extract()[0],
            'paperno': response.css('#metadata dl dd[1]').extract()[0],
            'subject': response.css('#metadata dl dd[2]').extract()[0],
            'breviate_keywords': response.css('#metadata dl dd[3]').extract()[0],
            'publisher': response.css('#metadata dl dd[4]').extract()[0],
            'breviate_page': response.css('#metadata dl dd[5]').extract()[0],
            'series': response.css('#metadata dl dd[6]').extract()[0],
            'start_page': response.css('#metadata dl dd[7]').extract()[0],
            'volume': response.css('#metadata dl dd[8]').extract()[0],
            'sub_volume': response.css('#metadata dl dd[9]').extract()[0],
            'session': response.css('#metadata dl dd[10]').extract()[0],
            'pages': response.css('#toolbar .pagination span.info').extract()[0],
        }


