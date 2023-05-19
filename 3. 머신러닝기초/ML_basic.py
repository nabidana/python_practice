import pandas as pd
import numpy as np
#model library 선언
from sklearn import datasets, tree

#모델 정확도 라이브러리 선언
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

#1. 데이터 전처리
featureData = pd.read_csv('./dataset/feature_regression_example.csv');
#데이터 타입 표준화해서 바꾸기
featureData['YEARWEEK']=featureData.YEARWEEK.astype(int)
featureData['YEAR']=featureData.YEAR.astype(int)
featureData['WEEK']=featureData.WEEK.astype(int)

#특성타입 추가해서 데이터타입 바꿔주기
#->feature 엔지니어링 이라고 부름
# case 1 : 바이너리맵사용
binaryMap = {"Y":1, "N":0}
featureData['HO_YN']=featureData.HOLIDAY.map(binaryMap)
featureData['PRO_YN']=featureData.PROMOTION.map(binaryMap)
# case 2 : np.where 사용(조건문)
#featureData['HO_YNM']=np.where(featureData.PROMOTION == "Y", 1 ,0)

#라벨인코더
#from sklearn.preprocessing import LabelEncoder
#객체를 만든다.
#ynLabelEn = LanelEncoder()

# >1 fit_transfrom 함수
#ynLabelEn.fit_transform(featureData["HOLIDAY"])
#HOLIDAY컬럼의 각 데이터를 알아서 매핑해서 encoding 시킨다.

# >2 inverse_transform 함수
#인코딩 시킨것을 다시 디코딩 시키는 작업.
#ynLabelEn.inverse_transform(featureData["HOLIDAY"])

#검증용
#colsdf1 = featureData.loc[ (featureData.HO_YNM == 1) & (featureData.PROMOTION !="Y")]
#colsdf2 = featureData.loc[ (featureData.HO_YNM == 0) & (featureData.PROMOTION !="N")]

import matplotlib.pyplot as plt
import seaborn as sns
#매직명령어. plt.show를 안써도 나오게하는거
#%matplotlib inline > 쥬피터랩에서만동작함.

#plt사이즈 정하기
#plt.figure(figsize=(5,3))
#데이터 차트화
sns.lmplot(data = featureData, x="QTY", y="PRO_PERCENT")
#plt showing 해주기. (시각화 그래프를 그려주는 것.)
#plt.show()

#차트를 그래프화 시켜서 보여주는것.
#sns.distplot(featureData["QTY"])

#2. 특성선정
#상관관계 확인하는것. 두 변수 간 선형적 혹은 비선형적 관계 분석하는것
corrDF = featureData.corr()
#print(corrDF)

#그래프차트로 한눈에보기위해서
#상관관계의 QTY컬럼만 불러옴
#QTY컬럼을 sort 시켜서 높은애부터 불러옴
qtyCorr = corrDF.loc[:,["QTY"]].sort_values(by=["QTY"], ascending=False)
#annot = true -> 숫자불러오기.
#heatmap 색깔별 그래프를 출력해주는것.
#sns.heatmap( qtyCorr, annot=True)
#sns.show()


#머신러닝일경우 튜닝된 기준값을 세팅하고 모델을 돌린다. 코릴레이션(상관관계)

stdCorrRepeat = np.array( list( range(3,8,1) ) ) / 10
stdCorr = 0.6
featurezz = list ( corrDF.loc[ (abs( corrDF.QTY) > stdCorr) & (abs( corrDF.QTY) != 1) ].index )

#참고용
#피어슨 구하기
#평균 값 먼저 구하기 -> avg = (a+b+c+d) /4
#편차 값 구하기(점수-평균) -> apan = a - avg || bpan = b - avg ...
#분산 값 구하기[(점수-평균)^2/개수] -> abun = (apan*apan)/4 || bbun = (bpan*bpan)/4
#분산 : 편차 제곱의 평균
#표준편차: 분산에 루트 적용해서 계산

#상관관계 계수 비율 선정하기
featuresStd = 0.5
#문제 대상 컬럼(특성 선정하기)
features = list(corrDF[ (abs(corrDF.QTY) > featuresStd) & (abs(corrDF.QTY) != 1)].index)
#print(features)

label = ['QTY']

#집어넣은 값을 8:2로 데이터를 알아서 랜덤하게 나누어서 결과를 줌
# *단 시간순서로 머신러닝을 돌려야할때는 적합하지않다. 왜냐면, 무작위로 데이터를 고르기 때문.
#from sklearn.model_selection import train_test_split
#random_state를 고정시키면 해당 값은 언제나 동일하게 고정되어 있다.
#trData,tdData = train_test_split(featureData, test_size=0.2, random_state=10)

#기계한테 학습시킬대 훈련 데이터는 약70퍼 센트만큼하고 나머지 30% 테스트 데이터로 나둔다.

stdRatio = 0.7
stdIndex = int( featureData.shape[0] * stdRatio)
#훈련문제지
trainingDataFeatures = featureData.loc[:stdIndex, features]
#훈련정답지
trainingDataLabel = featureData.loc[:stdIndex, label]
#테스트문제지
testDataFeatures = featureData.loc[stdIndex+1:, features]
#테스트정답지
testDataLabel = featureData.loc[stdIndex+1:, label]

#위와 동일한 방법
#날짜순으로 정렬을 해주어야함
sortKey = ["YEARWEEK"]
#정렬을 하고 기존 인덱스를 버리고 새로 인덱스를 부여한다.
sortedDate = featureData.sort_values(sortKey).reset_index(drop=True)
#최소 및 최대 치를 확인할수 있는것.
sortedDate.YEARWEEK.describe()

#날짜기준
stdyearweek = 2016
trainingDatafeautrez = featureData.loc[featureData.YEAR < stdyearweek, features]
trainingDatalabelz = featureData.loc[featureData.YEAR < stdyearweek, label]
testDatafeautrez = featureData.loc[featureData.YEAR > stdyearweek, features]
testDatalabelz = featureData.loc[featureData.YEAR > stdyearweek, label]
#인덱스기준
#indexNumzz = 0.7
#stdIndexz = int( featureData.shape[0] * indexNumzz)
# trainingDatafeautrez = featureData.loc[featureData.index < stdIndexz, features]
# trainingDatalabelz = featureData.loc[featureData.index < stdIndexz, label]
# testDatafeautrez = featureData.loc[featureData.index > stdIndexz, features]
# testDatalabelz = featureData.loc[featureData.index > stdIndexz, label]



# print(trainingDataFeatures.shape)
# print(trainingDataLabel.shape)
# print(testDataFeatures.shape)
# print(testDataLabel.shape)
#yearweeksdf = featureData['YEARWEEK'].sort_values()
#endcount = len(yearweeksdf) * 0.8
#print(yearweeksdf)
#print(endcount)

#print(featureData)
#print(colsdf2)
print()
#모델적용하기
#모델정의
model_method = tree.DecisionTreeRegressor(random_state=10) #random_state : 결과의 재현이 가능하도록 해줌
#머신러닝
model = model_method.fit(trainingDataFeatures, trainingDataLabel)
#model이 piclke파일로 저장됨. 그래서 나중에 그거 사용함

#예측해보기
predict = model.predict(testDataFeatures)

#예측결과 데이터프레임으로 변환
testDataLabel['PREDICT_DT']=predict
#print(testDataLabel)

#미래예측방법
inputHclus = 1 #휴일 -> 대휴일 : 1 // 소휴일 : 4
inputProPercent = 0.5 #프로모션비율
inputPromotionLB = 1 #프로모션 적용 Y
inputHlb = 1 #홀리데이 적용 Y

testDt = pd.DataFrame([ [inputHclus, inputProPercent, inputPromotionLB, inputHlb]])
rssa = model.predict(testDt)
#print()
#print(rssa)

from sklearn.tree import plot_tree
import matplotlib.pyplot as plt
plt.figure(figsize=(13, 8))
plot_tree(model)

