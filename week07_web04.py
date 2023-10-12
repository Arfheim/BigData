import urllib.request
from bs4 import BeautifulSoup

api = "https://www.kma.go.kr/weather/forecast/mid-term-rss3.jsp"
urls = urllib.request.urlopen(api).read()
soup = BeautifulSoup(urls,"html.parser")

cities = soup.find_all("city")
data = soup.find_all("data")
dates = soup.find_all("tmef")

#print(dates.string)

for i in range(len(cities)):
    print(f'{dates[i*13].string}시 기준으로 {cities[i].string}의 날씨는 {data[i*13].find("wf").string}입니다.')

print(len(cities), len(data))