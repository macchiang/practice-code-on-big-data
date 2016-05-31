req=requests.get("http://edition.cnn.com/tech")
html=req.text
soup=BeautifulSoup(html)
for lines in soup.select('.cd__content'):
    print lines.select('.cd__headline-text')[0].text
