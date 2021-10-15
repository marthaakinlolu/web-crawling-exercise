import scrapy



class GlobalVoiceSpider(scrapy.Spider):
    name = "yorubavoice_spider"
    start_urls = ['https://yo.globalvoices.org/']



    

    def parse(self, response):
        SET_SELECTOR = '.set'
        for globalvoice in response.css(SET_SELECTOR):
            
            NAME_SELECTOR = 'h1 ::text'
            yield {
                'name': globalvoice.css(NAME_SELECTOR).extract_first()
            }

        NEXT_PAGE_SELECTOR = '.next a ::attr(href)'
        next_page = response.css(NEXT_PAGE_SELECTOR).extract_first()
        if next_page:
            yield scrapy.Request(
                response.urljoin(next_page),
                callback=self.parse
        )

    FEED_FORMAT="csv"
    FEED_URI="yoruba_voice.csv"