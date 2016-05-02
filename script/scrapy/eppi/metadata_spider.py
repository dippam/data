import scrapy
import re

# A Scrapy spider to download the metadata for the EPPI document collection.
class EppiSpider(scrapy.Spider):
    name = 'eppi_spider'

    # Fetch directory of all EPPI documents -- 10292 in total.
    # A html partial is returned containing a JSON facet description and HTML document headers.
    # We ignore the JSON and iterate over the document headers.
    start_urls = ['http://www.dippam.ac.uk/eppi/results?search%5Bper_page%5D=10292&search%5Bpage%5D=1&search%5Btotal_pages%5D=&search%5Bview%5D=list&search%5Bqclean%5D=&search%5Bq%5D=%0A&search%5Bfields%5D=fulltext&search%5Bchrono%5D=on&search%5Bfrom%5D=1801&search%5Bto%5D=1922&search%5Bcat%5D%5B0%5D=on&search%5Bcat%5D%5B1%5D=on&search%5Bcat%5D%5B2%5D=on&search%5Bcat%5D%5B3%5D=on&search%5Bcat%5D%5B4%5D=on&search%5Bsort%5D=title&search%5Bsort_dir%5D=asc']

    # Parse the metadata directory.
    def parse(self, response):
        for href in response.css('#list .result h3 a::attr(href)'):
            full_url = response.urljoin(href.extract())
            yield scrapy.Request(full_url, callback=self.parse_document)

    # Snarf the dd elements from the metadata list.
    # Pages is stored in the pagination section of the #toolbar.
    def parse_document(self, response):
        dts = response.css('#metadata dl dt::text')
        dds = response.css('#metadata dl dd::text')
        metadata = {
            'id': response.url.split('/')[-1],
            'title': response.css('h1.title::text')[0].extract(),
            'pages': re.match(r"\d+", response.css('#toolbar .pagination span.info::text')[0].extract()).group()
        }

        for i in range(len(dts)):
          dt = dts[i].extract().lower().replace(' ', '_') # Convert to snake_case.
          dd = dds[i].extract()
          metadata[dt] = dd
        
        yield metadata





        
