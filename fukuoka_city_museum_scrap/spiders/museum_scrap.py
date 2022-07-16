from typing import Collection
import scrapy


class MuseumScrapSpider(scrapy.Spider):
    name = 'museum_scrap'
    allowed_domains = ['www.fukuoka-art-museum.jp']
    start_urls = ['https://www.fukuoka-art-museum.jp']

    def parse(self, response):
        #URL
        next_ex_pages = ('https://www.fukuoka-art-museum.jp/exhibition')
        next_premodern_pages = ('https://www.fukuoka-art-museum.jp/collection/?q=premodern')
        next_modern_pages = ('https://www.fukuoka-art-museum.jp/collection/?q=modern')
        
        yield response.follow(url=next_ex_pages, callback=self.parse_ex_items)
        yield response.follow(url=next_premodern_pages, callback=self.parse_items)
        yield response.follow(url=next_modern_pages, callback=self.parse_items)

        #exhabtion
    def parse_ex_items(self, response):
        
        main_now = response.xpath('//div')
        yield{
            'title':main_now.xpath('./div[1]/article[1]/div/h2[1]/text()').get(),
            'URL':main_now.xpath('./div[1]/article/a/@href').get(),
            'date':self.get_date(main_now.xpath('./div[1]/article[1]/div/p[1]/text()[1]').get())
            }
       
        main_features = response.xpath('//div[@id="ex_top_upcoming"]/article')
        for main_feature in main_features:         
            yield{
                'title':main_feature.xpath('./article/div[@class="ex_thumb_info"]/h2[1]/text()').get(),
                'URL':main_feature.xpath('.a/@href').get(),
                'date':self.get_date(main_feature.xpath('./div/p[1]/text()[1]').get())
                }
        
        ##modern,premodern
    def parse_items(self, response):
        
        moderns = response.xpath('//div[@id="ex_single_info"]')
        for modern in moderns:
            yield{
                'title': modern.xpath("./h1/text()").get(),
                'date': self.get_date(modern.xpath("./table/tbody/tr[1]/td/text()").get()),
                'time': self.get_date(modern.xpath("./table/tbody/tr[2]/td/text()").get()),
                'close': modern.xpath("./table/tbody/tr[3]/td/text()").get(),
            }

    def get_date(self, date):
        if date:
            return date.replace('\r\n','').replace(' ','')
        return date
    