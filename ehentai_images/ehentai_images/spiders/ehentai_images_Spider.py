from scrapy.spiders import Spider
from scrapy.selector import Selector
from scrapy import Request

from ehentai_images.items import EhentaiImagesItem

class ehentaiImagesSpider(Spider):
	"""抓黄图的"""
	name = "ehentai_images_spider"

	# allowed_domains = ["e-hentai.org"]
	download_delay = 1.5
	start_urls = [
		"https://e-hentai.org/g/1112447/530431657d/",
		"https://e-hentai.org/g/1102866/93382f91b2/",
		"https://e-hentai.org/g/1118551/1dff0183dd/",
		"https://e-hentai.org/g/1118480/7a4d2d9419/",
		"https://e-hentai.org/g/1118102/a3051b5cdd/",
		"https://e-hentai.org/g/1116918/f13a72ec73/",
		
	]

	def parse(self, response):
		sel = Selector(response)

		index = -1
		items = sel.xpath('//div[@class="gdtm"]')
		for item in items:
			index += 1
			site = item.xpath('div/a/@href').extract()
			yield Request(site[0], meta={'index': str(index)}, callback=self.parse_image)
	def parse_image(self, response):
		sel = Selector(response)

		image = sel.xpath('//div[@id="i3"]/a/img/@src').extract()
		title = sel.xpath('//h1/text()').extract()
		yield Request(image[0], meta={'image_title': title[0], 'image_name': response.meta['index']}, callback=self.parse_pic)
	def parse_pic(self, response):
		item = EhentaiImagesItem()
		item['image_title'] = response.meta['image_title']
		item['image_name'] = response.meta['image_name']
		item['image_content'] = response.body
		return item
		
