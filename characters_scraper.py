import scrapy

"""
 Here's the code for a spider that scrapes animation characters from a wikipedia page.
 Run the spider using the command (in the CLI) : scrapy runspider characters_scraper.py -o characters.json
"""
class CharacterSpider(scrapy.Spider):
    name = 'character_spider'
    start_urls = ['https://fr.wikipedia.org/wiki/Cat%C3%A9gorie:Personnage_d%27animation']

    def parse(self, response):
        for link in response.css('div#mw-pages div.mw-content-ltr li'):
            yield {'character': link.css('a::text').extract_first() }

        next_page = response.css('li.next a::attr("href")').get()
        if next_page is not None:
            yield response.follow(next_page, self.parse)
