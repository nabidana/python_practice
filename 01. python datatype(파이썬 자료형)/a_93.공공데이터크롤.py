import pandas as pd

# testurl1 = "https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId=FILE_000000002579913&fileDetailSn=1&dataNm=%ED%95%9C%EA%B5%AD%EB%B6%80%EB%8F%99%EC%82%B0%EC%9B%90_%EC%98%A4%ED%94%BC%EC%8A%A4%ED%85%94%20%EA%B0%80%EA%B2%A9%EB%8F%99%ED%96%A5%EC%A1%B0%EC%82%AC_%EC%A0%84%EC%84%B8%EA%B0%80%EA%B2%A9(%EC%A7%80%EC%97%AD%EB%B3%84)_20220630"
# testdata1 = pd.read_csv(testurl1, encoding='ms949')
# print(testdata1.tail())


import requests
jsonurl1 = "https://kosis.kr/openapi/Param/statisticsParameterData.do?method=getList&apiKey=Y2VkZjJjZTY0MDYwN2RjM2FmODc3NmEwYWI2OWE5OGU=&itmId=13103890822T1+&objL1=10+&objL2=&objL3=&objL4=&objL5=&objL6=&objL7=&objL8=&format=json&jsonVD=Y&prdSe=M&newEstPrdCnt=3&orgId=101&tblId=DT_1YL20881E"
jsondata1 = pd.DataFrame()
try:
    response = requests.get(jsonurl1)
    if response.status_code==200:
        jsondata1=pd.read_json(jsonurl1)    #json 파일 가져오기.
    else:
        response.close()
except Exception as e:
    print(e)
    
print(jsondata1)
#lmxl install 필요
#pip install lxml --force -U
from lxml import html
from bs4 import BeautifulSoup
from urllib.request import Request, urlopen
from urllib.parse import urlencode, quote_plus, unquote

API_KEY1 = unquote('key')
xmlurl1 = 'http://openapi.molit.go.kr:8081/OpenAPI_ToolInstallPackage/service/rest/RTMSOBJSvc/getRTMSDataSvcAptTrade?_wadl&type=xml'
params ={'serviceKey' : 'r5z9cSGxBw3flF/iPNPA/CRDALGfknexgqqn0QBTQUX6rxHHL+cyDtKjNOevcHo3f6N0yWOm4sfQv8+a/Q2TFQ==', 'LAWD_CD' : '11110', 'DEAL_YMD' : '201512' }
# queryParams = '?'+urlencode(
#     {
#         quote_plus('ServiceKey'):API_KEY1,
#         quote_plus('LAWD_CD'):'11110',
#         quote_plus('DEAL_YMD'):'201512'
#     }
# )
# response1 = requests.get(xmlurl1 + params)
response1 = requests.get(xmlurl1, params=params)
response1.encoding='utf8'
xmlobj = BeautifulSoup(response1.text,"lxml-xml")
#print(xmlobj)

#rows=xmlobj.findAll('items')
row_list = [] # 행값
name_list = [] # 열이름값
value_list = [] #데이터값
rows = xmlobj.findAll('item')
# xml 안의 데이터 수집
for i in range(0, len(rows)):
    columns = rows[i].find_all()
    #첫째 행 데이터 수집
    for j in range(0,len(columns)):
        if i ==0:
            # 컬럼 이름 값 저장
            name_list.append(columns[j].name)
        # 컬럼의 각 데이터 값 저장
        value_list.append(columns[j].text)
    # 각 행의 value값 전체 저장
    row_list.append(value_list)
    # 데이터 리스트 값 초기화
    value_list=[]
    
corona_df = pd.DataFrame(row_list, columns=name_list)
print(corona_df.head(19))
