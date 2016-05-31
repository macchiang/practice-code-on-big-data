import scrapy
from bs4 import BeautifulSoup

class AppleCrawler(scrapy.Spider):
	name='apple'
	start_urls=['http://www.appledaily.com.tw/realtimenews/section/new/']
	def parse(self,response):
		domain_name="http://www.appledaily.com.tw"
		res=BeautifulSoup(response.body)
		for news in res.select('.rtddt'):
			print news.select('h1')[0].text
			print news.select('a')[0]['href']
