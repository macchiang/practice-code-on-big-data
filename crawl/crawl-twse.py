req=requests.get("http://www.twse.com.tw/ch/trading/fund/BFI82U/BFI82U.php?report1=day&input_date=105%2F05%2F31&mSubmit=%ACd%B8%DF&yr=2016&w_date=20160530&m_date=20160501")
req.encoding='utf-8'
html=req.text.encode('utf-8')
soup=BeautifulSoup(html,"html.parser")
for td in soup.findAll("td",{"class":"basic2"}):
    print td.text
