import scrapy
import re
from maple.items import MapleItem

class MapleSpider(scrapy.Spider):
	name = "maple"
	allowed_domains = ["ontariomaple.com"]
	start_urls = ["http://www.ontariomaple.com/pages/farmgate/"]
	
	def parse(self, response):
		for url in response.xpath('//map/area/@href').extract():
			yield scrapy.Request(url, callback=self.get_data)
	
	def get_data(self, response):
		region = response.xpath('//h1[@class="pageHeader"]/text()').extract()
		#items = []
		for listing in response.xpath('//div[@class="directory looking2"]'):
			item = MapleItem()
			item['region'] = region
			item['name'] = listing.xpath('h4/text()').extract()
			for link in listing.xpath('*/a/@href').extract():
				pieces = link.split("mailto:",1)
				if len(pieces) == 2:
					item['email'] = pieces[1]
				else:
					item['web'] = pieces[0]
			addressfound = None
			address = ""
			blurb = ""
			for needle in listing.xpath('.//text()').extract():
				blurb = blurb+needle
				#print needle
				if addressfound == True:
					address = address + "<br/>" + needle
					item['address'] = address
					addressfound = None
				else:
					match = re.search("[0-9]{3}(-| )[0-9]{3}(-| )[0-9-]*", needle)
					if match is not None:
						item['phone'] = match.group()
					match = re.match("[0-9]+ [A-Z]", needle)
					if match is not None:
						#print "found address: ", needle
						addressfound = True
						address = needle
					match = re.search("[A-Z]{1}[0-9]{1}[A-Z]{1} [0-9]{1}[A-Z]{1}[0-9]{1}", needle)
					if match is not None:
						item['postalcode'] = match.group()
				item['blurb'] = blurb.replace("\r\n","<br/>")
			#items.append(item)
			#print item['region'], ' - ', item['name']
			yield item