# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
#  from scrapy.contrib.spiders import CrawlSpider, Rule
#  from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor
from ucblibrary.items import UcbLibraryItem  # This is the item I defined in items.py


#class MultiPagesSpider(CrawlSpider):
class LibrarySpider(BaseSpider):
    '''spiders lib hours, follows links'''
    name = 'library'
    domain_name = 'lib.berkeley.edu'
    allowed_domains = ['lib.berkeley.edu']
    start_urls = ['http://www.lib.berkeley.edu/hours/front/info?library_id=253', ]
    # rules = (Rule(SgmlLinkExtractor(allow=('/hours/front/info\?library_id=\d+', )),
    #   callback='parse_item', follow= True),)

#html/body/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[2]
#html/body/table/tr/td[1]/table/tr[2]/td/p[2]

#to get calendar title 'antro library'
#/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/h1
#to get month date
#/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table/thead/tr[1]/td/span[3]/h1
<<<<<<< HEAD

    def parse(self, response):   # remember to rename when using multipage spider b/c name errors
        hxs = HtmlXPathSelector(response)
        scraped_items = []
        scraped_item = UcbLibraryItem()
        #scraped_item['name'] = hxs.select('/html/body/table/tr/td[1]/table//tr[1]/td[2]/p[1]/a[@href][1]/text()').extract()
        #scraped_item['url'] = hxs.select('/html/body/table/tr/td[1]/table//tr[1]/td[2]/p[1]/a/@href[1]').extract()
        scraped_item['library_id'] = response.url.split('=')[2]   # picking out the library id fromt the url
        scraped_item['name'] = hxs.select('/html/body/table/tr[2]/td/table/tr/td/h1')

        day = hxs.select('//table[@class="cal"]//td[@class="calendar_numeral"]/h1/text()').extract()
        hours = hxs.select('//table[@class="cal"]//td[@class="calendar_description"]//h6/self::*').re(r'<h6>\n\n\s*(.*)\n\n</h6>')
        hours = [x.replace('<br>', ' ') for x in hours]
        day_hours = dict(zip(day, hours))
        scraped_items.append(scraped_item)
        # for item in items:
        #   scraped_item = UcbLibraryItem() ### this is the item object you defined in the items file
        #   #hxs.select('/html/body/table/tr/td[1]/table//tr[1]/td[2]/p[1]/a[@href][1]/text()').extract()
        #   scraped_item["name"] = item.select('td[2]/p[1]/a[@href][1]/text()').extract() ### assuming your item object has “title” field
        #   scraped_items.append(scraped_item)
        return(scraped_items)

spider = LibrarySpider()  # spider = MultiPagesSpider()
=======
#

	def parse(self, response):  #remember to rename when using multipage spider b/c name errors
		hxs = HtmlXPathSelector(response)
		hours = hxs.select('/html/body/table/tbody/tr/td[1]/table//tr')
		scraped_items = []
		scraped_item = UcbLibraryItem()
		#scraped_item['name'] = hxs.select('/html/body/table/tr/td[1]/table//tr[1]/td[2]/p[1]/a[@href][1]/text()').extract()
		#scraped_item['url'] = hxs.select('/html/body/table/tr/td[1]/table//tr[1]/td[2]/p[1]/a/@href[1]').extract()
		scraped_item['library_id'] = response.url.split('=')[2] #picking out the library id fromt the url
		scraped_item['name'] = hxs.select('//td[@valign="top"]/h1/text()').extract()[0]
		scraped_items.append(scraped_item)
		day=hxs.select('//table[@class="cal"]//td[@class="calendar_numeral"]/h1/text()').extract()
		day = [int(x) for x in day]
		hours = hxs.select('//table[@class="cal"]//td[@class="calendar_description"]//h6/self::*').re(r'<h6>\n\n\s*(.*)\n\n</h6>')
		hours = [x.replace('<br>',' ') for x in hours]
		day_hours = dict(zip(day,hours))
		# for item in items:
		# 	scraped_item = UcbLibraryItem() ### this is the item object you defined in the items file
		# 	#hxs.select('/html/body/table/tr/td[1]/table//tr[1]/td[2]/p[1]/a[@href][1]/text()').extract()
		# 	scraped_item["name"] = item.select('td[2]/p[1]/a[@href][1]/text()').extract() ### assuming your item object has “title” field
		# 	scraped_items.append(scraped_item)
		return(scraped_items)

spider = LibrarySpider()
#spider = MultiPagesSpider()
>>>>>>> d79b2dbc998124280fe08a56a07fd3fe8e0dddb2
