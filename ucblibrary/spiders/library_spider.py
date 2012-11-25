# coding: utf-8

from scrapy.selector import HtmlXPathSelector
from scrapy.contrib.spiders import CrawlSpider, Rule
from scrapy.contrib.linkextractors.sgml import SgmlLinkExtractor 
from ucblibrary.items import UcbLibraryItem ##This is the item I defined in items.py

class MultiPagesSpider(CrawlSpider):
	'''spiders lib hours, follows links'''
	name = 'library'
	domain_name = 'lib.berkeley.edu'
	allowed_domains = ['lib.berkeley.edu']
	start_urls = ['http://www.lib.berkeley.edu/hours',]
	rules = (Rule(SgmlLinkExtractor(allow=('/hours/front/info\?library_id=\d+', )), 
		callback='parse_item', follow= True),)

#/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr/td[4]/a
#/html/body/table/tbody/tr[2]/td/table/tbody/tr/td/table[2]/tbody/tr[3]/td[4]/a

	def parse_item(self, response):
		hxs = HtmlXPathSelector(response)
		items= hxs.select('/html/body/ul')
		scraped_items =[]
		for item in items:
			scraped_item = UcbLibraryItem() ### this is the item object you defined in the items file
			scraped_item["name"] = item.select('li/text()').extract() ### assuming your item object has “title” field
			scraped_items.append(scraped_item)
		return(items)

spider = MultiPagesSpider()