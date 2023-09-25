import requests
from bs4 import BeautifulSoup

keyword = input("검색할 키워드를 입력하세요.")
page = int(input("검색할 페이지를 입력하세요."))
pageNum = 1

for i in range(1, page*10, 10):
  print(f"=========== {pageNum}페이지 ===========")
  response = requests.get(f"https://search.naver.com/search.naver?where=news&ie=utf8&sm=nws_hty&query={keyword}&start={i}")
  html = response.text
  soup = BeautifulSoup(html, 'html.parser')
  datas = soup.select('.news_tit')
  for i in range(len(datas)):
    title = datas[i].text
    url = datas[i].attrs['href']
    print(title, end="")
    print(url)

  pageNum += 1
