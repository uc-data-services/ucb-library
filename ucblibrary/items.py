# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/topics/items.html

from scrapy.item import Item, Field


class UcbLibraryItem(Item):
    # define the fields for your item here like:
    name = Field()
    # url = Field()
    library_id = Field()
    """desc = Field()
    image = Field()
    address = Field()
    telephone = Field()
    branchOf = Field()"""
    hours = Field()
