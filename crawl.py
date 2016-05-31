// craw ptt post
import requests
from bs4 import BeautifulSoup
req=requests.get("https://www.ptt.cc/bbs/HatePolitics/index.html")
html=req.text.encode('utf-8')
soup=BeautifulSoup(html,"html.parser")
for rents in soup.select('.r-ent'):
    print rents.select('.title')[0].text.encode('utf-8')
    print rents.select('.date')[0].text.encode('utf-8')
    print rents.select('.author')[0].text.encode('utf-8')
