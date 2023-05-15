import pandas as pd
import numpy as np
#model library 선언
from sklearn import datasets, tree

#모델 정확도 라이브러리 선언
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error

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

#검증용
#colsdf1 = featureData.loc[ (featureData.HO_YNM == 1) & (featureData.PROMOTION !="Y")]
#colsdf2 = featureData.loc[ (featureData.HO_YNM == 0) & (featureData.PROMOTION !="N")]
#상관관계 확인하는것. 두 변수 간 선형적 혹은 비선형적 관계 분석하는것
corrDF = featureData.corr()
print(corrDF)

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
print(features)

label = ['QTY']

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
print(testDataLabel)

#미래예측방법
inputHclus = 1 #휴일 -> 대휴일 : 1 // 소휴일 : 4
inputProPercent = 0.5 #프로모션비율
inputPromotionLB = 1 #프로모션 적용 Y
inputHlb = 1 #홀리데이 적용 Y

testDt = pd.DataFrame([ [inputHclus, inputProPercent, inputPromotionLB, inputHlb]])
rssa = model.predict(testDt)
print()
print(rssa)
