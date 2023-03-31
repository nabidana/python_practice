import requests
from bs4 import BeautifulSoup
import pandas as pd
import re

baseurl = "https://www.coupang.com/np/search?component=&q=%EC%B2%AD%EC%B6%95+%ED%82%A4%EB%B3%B4%EB%93%9C&channel=user"
mainheaders = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36", "Accept-Language": "ko-KR,ko;q=0.8,en-US;q=0.5,en;q=0.3"}
resdata = requests.get(baseurl, headers=mainheaders)
resdata.raise_for_status() # 웹페이지의 상태가 정상인지 확인

beutipage = BeautifulSoup(resdata.text, "lxml")
items = beutipage.find_all("li", attrs={"class":re.compile("^search-product")}) # li 태그 중에서 class 옵션이 search-product로 시작하는 요소들만 가져온다.

itemList = []
for i in range( len(items)) :
    itemName = items[i].find("div", attrs={"class" : "name"}).get_text()
    itemPrice = items[i].find("strong", attrs={"class" : "price-value"}).get_text()
    itemList.append([itemName, itemPrice])

print()
myItems = pd.DataFrame(itemList, columns={"상품이름", "상품가격"})
print(myItems)

#결과
#                                                 상품이름     상품가격
#0     앱코 HACKER K840 화이트 블랙 청축 조약돌+G102 IC 게이밍 마우스 세트   79,500
#1   COX 축교환식 레인보우 LED 기계식 게이밍 키보드 청축, 일반형, CK420, 화이트   40,400
#2    COX 축교환식 레인보우 LED 기계식 게이밍 키보드 청축, 일반형, CK420, 블랙   40,400
#3        앱코 축교환 레인보우 무빙 LED 기계식 키보드 청축, 블랙, K560, 일반형   30,500
# .....................
