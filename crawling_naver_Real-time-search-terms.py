import requests
from bs4 import BeautifulSoup

# 유저 설정
headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/86.0.4240.198 Safari/537.36'}

# 네이버 메인이 아닌 DataLab 페이지
url = 'https://datalab.naver.com/keyword/realtimeList.naver?where=main'

# User 설정
res = requests.get(url, headers = headers)

# res.content 주의
soup = BeautifulSoup(res.content, 'html.parser')

# span.item_title 정보를 선택
data = soup.select('span.item_title')

cnt = 1
for item in data:
  print(str(cnt) + ". " + item.get_text())
  cnt += 1
