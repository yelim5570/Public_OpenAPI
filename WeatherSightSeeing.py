#http://newsky2.kma.go.kr/service/TourSpotInfoService/SpotShrtData?serviceKey=y80jnESQZu1%2B%2BKrpWpkGrnZ96%2FhiBicuIH%2F3SeO0u10CK9rglO3nqmwetj8%2BRHj%2F1NWUUis4aeGnUMk1CFUYRQ%3D%3D&HOUR=24&COURSE_ID=1&pageNo=1&numOfRows=10&CURRENT_DATE=2019120101


import urllib.request as ul
import xml.etree.ElementTree as ET

key = "y80jnESQZu1%2B%2BKrpWpkGrnZ96%2FhiBicuIH%2F3SeO0u10CK9rglO3nqmwetj8%2BRHj%2F1NWUUis4aeGnUMk1CFUYRQ%3D%3D"
date = "2020020101"
url = "http://newsky2.kma.go.kr/service/TourSpotInfoService/SpotShrtData?serviceKey="+ key +"&HOUR=24&COURSE_ID=1&pageNo=1&numOfRows=10&CURRENT_DATE=" + date

# 데이터를 받을 url
request = ul.Request(url)
# url의 데이터를 요청함
response = ul.urlopen(request)
# 요청받은 데이터를 열어줌
rescode = response.getcode()

# 제대로 데이터가 수신됐는지 확인하는 코드 성공시 200
if (rescode == 200):
    responseData = response.read()
    # 요청받은 데이터를 읽음
    rD = ET.fromstring(responseData)
    # XML형식의 데이터를 dict형식으로 변환시켜줌

    #print(rD.tag)
    # 정상적으로 데이터가 출력되는지 확인

    for item in rD.iter('item'):
        spotName = item.find('spotName').text
        ws = item.find('ws').text
        thema = item.find('thema').text
        print (spotName + ", " +ws +"," +thema)

