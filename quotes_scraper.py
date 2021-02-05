import scrapy

"""
Here's the code for spider that scrapes famous quotes from website http://quotes.toscrape.com, following the pagination.
Run the spider using the runspider command (in the CLI) : scrapy runspider quotes_scraper.py -o quotes.json
"""

class QuotesSpider(scrapy.Spider):
	name = 'quotes'
	start_urls = ['http://quotes.toscrape.com/tag/humor/']

	def parse(self, response):
		for quote in response.css('div.quote'):
			yield {
				'author': quote.xpath('span/small/text()').get(),
				'text': quote.css('span.text::text').get()
			}
		next_page = response.css('li.next a::attr("href")').get()
		if next_page is not None:
			yield response.follow(next_page, self.parse)