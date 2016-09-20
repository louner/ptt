import scrapy

chineseNextPage = u'\u2039 \u4e0a\u9801'
pttDomain = 'https://www.ptt.cc'

def addPttDomain(url):
    return '%s%s'%(pttDomain, url)

class StackOverflowSpider(scrapy.Spider):
    name = 'ptt'
    start_urls = ['https://www.ptt.cc/bbs/c_chat/index.html']

    def parse(self, response):
        yield {'crawled': response.url}
        pageUrls = response.xpath('//div[@class="title"]/a/@href').extract()
        for pageUrl in pageUrls:
            pageUrl = addPttDomain(pageUrl)
            yield scrapy.Request(pageUrl, callback=self.collectMessages)

        for a in response.selector.xpath('//a[@class="btn wide"]'):
            if a.xpath('text()').extract()[0] == chineseNextPage:
                nextPageUrl = addPttDomain(a.xpath('@href').extract()[0])
                yield scrapy.Request(nextPageUrl, callback=self.parse)

    def collectMessages(self, response):
        yield {'crawled': response.url}
        messages = response.xpath('//div[@class="push"]')
        for message in messages:
            sentiment = message.xpath('span[contains(@class, "hl push-tag")]/text()').extract()[0]
            sentences = message.xpath('span[contains(@class, "push-content")]/text()').extract()[0]
            yield {'sentiment': sentiment, 'sentences': sentences}
        
