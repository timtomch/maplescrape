import scrapy

class MapleSpider(scrapy.Spider):
	name = "maple"
	allowed_domains = ["ontariomaple.com"]
	start_urls = ["http://www.ontariomaple.com/pages/farmgate/"]
	
	def parse(self, response):
		for sel in response.xpath('//map/area/@href').extract():
			print sel
		