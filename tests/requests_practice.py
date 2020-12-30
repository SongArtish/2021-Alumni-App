import requests

webpage = requests.get("http://www.naver.com/")
print(webpage.text)