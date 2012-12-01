# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.spider import BaseSpider
#from scrapy.contrib.spiders import CrawlSpider, Rule
#from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor 
from ucblibrary.items import UcbLibraryItem ##This is the item I defined in items.py

#class MultiPagesSpider(CrawlSpider):
class LibrarySpider(BaseSpider):
	'''spiders lib hours, follows links'''
	name = 'library'
	domain_name = 'lib.berkeley.edu'
	allowed_domains = ['lib.berkeley.edu']
	start_urls = ['http://www.lib.berkeley.edu/hours/front/info?library_id=253',]
	# rules = (Rule(SgmlLinkExtractor(allow=('/hours/front/info\?library_id=\d+', )), 
	# 	callback='parse_item', follow= True),)

#html/body/table/tbody/tr/td[1]/table/tbody/tr[1]/td/table/tbody/tr/td[2]
#html/body/table/tr/td[1]/table/tr[2]/td/p[2]

	def parse(self, response):  #remember to rename when using multipage spider b/c name errors
		hxs = HtmlXPathSelector(response)
		#items = hxs.select('/html/body/table/tbody/tr/td[1]/table//tr')
		scraped_items = []
		scraped_item = UcbLibraryItem()
		scraped_item['name'] = hxs.select('/html/body/table/tr/td[1]/table//tr[1]/td[2]/p[1]/a[@href][1]/text()').extract()
		scraped_item['url'] = hxs.select('/html/body/table/tr/td[1]/table//tr[1]/td[2]/p[1]/a/@href[1]').extract()
		scraped_item[''] =
		scraped_items.append(scraped_item)
		# for item in items:
		# 	scraped_item = UcbLibraryItem() ### this is the item object you defined in the items file
		# 	#hxs.select('/html/body/table/tr/td[1]/table//tr[1]/td[2]/p[1]/a[@href][1]/text()').extract()
		# 	scraped_item["name"] = item.select('td[2]/p[1]/a[@href][1]/text()').extract() ### assuming your item object has “title” field
		# 	scraped_items.append(scraped_item)
		return(scraped_items)

spider = LibrarySpider()
#spider = MultiPagesSpider()