import requests
from bs4 import BeautifulSoup
import re

webpage = requests.get("http://www.naver.com/")
soup = BeautifulSoup(webpage.content, "lxml")

## 1. 웹 페이지 전체 탐색
# print(soup)
## 2. 특정 태그 탐색
# print(soup.h2)
## 3. 태그 내용 탐색
# print(soup.span.string)
## 4. 태그 트리구조 탐색
# for child in soup.ul.children:
#     print(child.string)
# for parent in soup.html.parents:
#     print(parent)

### .find_all()
## 1. 기본
# print(soup.find_all("h2"))
# print(type(soup.find_all("h2")))
## 2. 정규식
# import re
# print(soup.find_all(re.compile("[ou]l")))
# print(soup.find_all(re.compile("h[1-9]")))
## 3. 리스트
# print(soup.find_all(['h1', 'p']))
## 4. html 속성
print(soup.find_all(attrs={'class':'column_left'}))