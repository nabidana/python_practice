#셀레니움설치 : pip install selenium
#웹드라이버매니저는 따로 설치해야함 : pip install webdriver-manager

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 드라이버 위치 설정
def setChromeDriver():
    options = Options() #웹드라이버의크롬옵션을 사용
    user_agent = 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/100.0.4896.75 Safari/537.36'
    options.add_argument('user-agent=' + user_agent)
    options.add_experimental_option("detach", True) #브라우저 자동종료 방지
    # options.add_argument('--headless') # 웹 브라우저를 시각적으로 띄우지 않는 headless chrome 옵션
    driver = webdriver.Chrome(service=Service(executable_path=ChromeDriverManager().install()), options=options)
    return driver
    #executable_path : 실행하는 파일의 위치

driver = setChromeDriver()
# 웹페이지 파싱 될때까지 최대 3초 기다림
driver.implicitly_wait(3)

driver.get("https://www.google.co.kr/")
googleInputXpath = '/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input'    #검색창XPATH
driver.find_element(By.XPATH, googleInputXpath).send_keys("selenium")   #검색창에 "selenium" 입력하는것
driver.find_element(By.XPATH, googleInputXpath).send_keys(Keys.ENTER)   #엔터버튼을 클릭하는 것

htmlObj = driver.page_source
from bs4 import BeautifulSoup
bsObj = BeautifulSoup(htmlObj, "html.parser")
print(bsObj)

import smtplib  #smtp서비스 라이브러리
from email.message import EmailMessage  #이메일 메세지 라이브러리

smtp_gmail = smtplib.SMTP('smtp.gmail.com',587) #SMTP서버 및 포트 설정
smtp_gmail.ehlo()   #서버연결 설정 함수
smtp_gmail.starttls()   #서버 연결 암호화

import getpass
myinput = getpass.getpass() #패스워드를 숨기기위해서.

#계정정보 입력
userid = "Admin"
userpw = "PASSWORD"
smtp_gmail.login(userid, userpw)
import pandas as pd
mailList = pd.read_csv("E:/VScodefd/Python/testemaillist.csv")
mlis = mailList.tolist()

file='filename.e'
fp = open(file, 'rb')   #파일을 불러와서 읽는것
file_data=fp.read()

msgg = EmailMessage()
msgg['Subject']="QUIZ NAME" #제목
msgg.set_content("QUIZ INFORMATION")    #내용
msgg['From']="TEST@TSET.COM"    #보내는사람
msgg['To']=",".join(mlis)   #받는사람

msgg.add_attachment(file_data, maintype='text',subtype='plain',filename=file)

smtp_gmail.send_message(msgg)   #메일전송
smtp_gmail.close

#3.pickle
import pickle
inPass = "QWWEGqegqekjfbqe"
#피클 파일 저장하기
with open("./testpk.pickle","wb") as fw :
    pickle.dump(inPass, fw) # fw : 파일쓰기

#피클 파일 읽기
with open("./testpk.pickle", "rb") as fr :  #rb : 읽기
    testData = pickle.load(fr)

print(testData)

urls = "요청주소"
json = pd.DataFrame()


import pandas as pd

targetURL = 'https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId=FILE_000000002633405&fileDetailSn=1&dataNm=%ED%95%9C%EA%B5%AD%EC%A3%BC%ED%83%9D%EA%B8%88%EC%9C%B5%EA%B3%B5%EC%82%AC_%EC%A3%BC%ED%83%9D%EA%B8%88%EC%9C%B5%EA%B4%80%EB%A0%A8%20%EC%A7%80%EC%88%98_20160101';
reading = pd.read_csv(targetURL, encoding="ms949")
print(reading)
print('--------------------------------')
print(reading.tail(2)) #꼬리부분 2개를 불러옴
print('--------------------------------')
print(reading.head(2)) # 머리부분 2개를 불러옴
print('--------------------------------')

carURL = 'https://raw.githubusercontent.com/hyokwan/python-lecture/master/dataset/cars.csv'
rancar = pd.read_csv(carURL, encoding="ms949")
print(rancar)

print("")
print('-------------------------')

testur = 'https://www.data.go.kr/cmm/cmm/fileDownload.do?atchFileId=FILE_000000002695643&fileDetailSn=1&dataNm=%ED%95%9C%EA%B5%AD%EB%B6%80%EB%8F%99%EC%82%B0%EC%9B%90_%EC%98%A4%ED%94%BC%EC%8A%A4%ED%85%94%20%EA%B0%80%EA%B2%A9%EB%8F%99%ED%96%A5%EC%A1%B0%EC%82%AC_%EC%A0%84%EC%84%B8%EA%B0%80%EA%B2%A9(%EC%A7%80%EC%97%AD%EB%B3%84)_%EA%B5%AC%ED%91%9C%EB%B3%B8(2018%EB%85%84-2020%EB%85%846%EC%9B%94)_20200630'
palm = pd.read_csv(testur, encoding='ms949')
print(palm.head(8))


#여기 못적음
#여기
#여기


