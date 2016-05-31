import scrapy
from bs4 import BeautifulSoup

class AppleCrawler(scrapy.Spider):
	name='apple'
	start_urls=['http://www.appledaily.com.tw/realtimenews/section/new/']
	def parse(self,response):
		res=BeautifulSoup(response.body)
		for news in res.select('.rtddt'):
			print news.select('h1')[0].text