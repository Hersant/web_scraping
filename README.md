# Overview
This repository provides codes for spiders that scrape animation characters from a wikipedia page and famous quotes from the website http://quotes.toscrape.com.

# Prerequisite
Install the framework Scrapy : https://scrapy.org/

# Running
- To scrape quotes : run the spider using the runspider command (in the CLI) : scrapy runspider quotes_scraper.py -o quotes.json
- to scrape animation characters : run the spider using the command (in the CLI) : scrapy runspider characters_scraper.py -o characters.json
