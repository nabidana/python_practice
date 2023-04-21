import pandas as pd
import requests, bs4

try :
    targetPG = requests.get("https://sparkkorea.com/퀴즈/");    #타겟페이지 설정
except Exception as e :
    print(e);
    
webPage = targetPG.text #타겟페이지의 텍스트를 가져옴
htmlPG = bs4.BeautifulSoup( webPage, "html.parser");    #가져온 페이지를 정보추출함수를 사용
findDiv = htmlPG.find(name = "div", attrs={"id" : "id_spark_quiz"}) #추출한곳에서 div를 딕셔너리 id에 해당하는 정보를 저장
findingAll = findDiv.findAll(name ="a") #저장한 정보에서 "a"로 시작하는것을 모두 찾아서 각 배열에 저장
quizList = []

for i in range( len(findingAll)) :
    quizname = findingAll[i].text   #저장한 곳에서 텍스트만 추출
    quizlink = findingAll[i].attrs["href"]  #저장한곳에서 href로 시작하는 URL만 추출
    quizList.append([quizname, quizlink])   #2차원배열에 저장
    
print()
findataList = pd.DataFrame( quizList, columns=["QUIZ", "NAME"]) #데이터프레임 이용해서 컬럼두개로 나누어서 출력
print(findataList)
