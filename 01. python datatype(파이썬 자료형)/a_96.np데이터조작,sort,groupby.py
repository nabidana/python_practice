import pandas as pd
import numpy as np

csdata = pd.read_csv("./dataset/customerdata.csv")
csdata["PRODUCT_AGE_NEW"] = np.where(csdata.PRODUCTAGE < 1, 1, np.where(csdata.PRODUCTAGE <= 2, 2, 3))
print(csdata)
#검증할 반대의 케이스도 있어야 한다.
#함수로 적용가능


# datafm = 데이터프레임 변수명

# 데이터의 건수와 컬럼수를 체크하기 위해서 사용하는 함수 : 
# datafm.shape()

# 데이터의 정보(컬럼과 몇개인지와 type)를 확인하기 위해서 사용하는 함수 : 
# datafm.info()

# 데이터의 값이 null인지 확인하는 함수 : 
# datafm.isnull()


# 교량형식이 거더교 아치교 사장교인것만 조회할때
# bridgeType = ["거더교", "아치교", "사장교"]

# datafm.loc[ (datafm.교량형식.isin(bridgeType) ]
# datafm.loc[ (datafm.교량형식 == "거더교") & (datafm.교량형식 == "아치교") & (datafm.교량형식 == "사장교")

# 인덱스번호가 뒤죽박죽인것을 0부터 다시 설정해주는방법
# datafm.reset_index(drop=True)

# 컬럼 조건에 따른 값 출력
# np.where(조건식, 참일때출력값, 거짓일때값)
csdata["AGE_NEW"] = np.where(csdata.PRODUCTAGE <= 1, 1, np.where(csdata.PRODUCTAGE <= 2, 2, 3))
print(csdata)
print("")
# 컬럼 조건에 따라서 값을 변경해서 출력
# datafm.loc[ (조건식), 대상컬럼]  = 값
csdata.loc[csdata.CUSTID=="A13566", "EMI"] = 10
print(csdata)
print("")
#파이썬은 동일데이터베이스 대비 속도가빠르고, 상이한 데이터 조작이 유용함.
#데이터간 컬럼문자 붙이기
#datafm[새로운컬럼]=datafm.컬럼.str[인덱스]+"_"+datafm.컬럼.astype(str)
csdata["NEW_CMS"] = csdata.CUSTID.str[1:]+"_"+csdata.EMI.astype(str)
print(csdata)
print("")

csdata["PRIDUCTAGE_NEW"] = np.where(csdata.PRODUCTAGE < 1, 1, np.where(csdata.PRODUCTAGE < 2, 2,\
        np.where(csdata.PRODUCTAGE < 3, 3, 5)))
print(csdata)
print("")

#보통 데이터는 디비를 통해 관리한다.
#특정컬럼제거
#list( set( 데이터프레임 ) ) - set( [특정컬럼명] )

#list : value를 추가하거나 업데이트하기 용이함
#set : value를 차집합 교집합 합집합 할때 용이함.

#데이터sort함수이용
#datafm.sort_values(by=[정렬컬럼]) >> 오름차순
#datafm.sort_values(by=[정렬컬럼], ascending=False) >> 내림차순(큰거부터아래로)
#datafm.sort_values(by=[정렬컬럼], ignore_index = True) >> ignore_index는 정렬후 인덱스도 정리해줌.
#컬럼두개 정렬
#datafm.sort_values(by=[컬럼1, 컬럼2], ascending=[True, False])

#데이터프레임 그룹으로 묶어서 분리하기
#datafm.groupby ( by=[컬럼명])[[값을 구할 컬럼]].mean()
#데이터프레임 group by 에서 사용할수 있는 함수
#1) 평균 : mean()   2)개수 : count()    3)최대 : max()  4)최소 : min   

dtfma = pd.read_csv("./dataset/customerdata.csv")
groupKey = ["EMI"]
print("전체",dtfma)

#아이템 전체 개수
csdta = dtfma.groupby(by=groupKey)["AVGPRICE"].agg(["count"])
print("cout : ",csdta)
print("")
#첫번째 아이템
asd1 = dtfma.groupby(by=groupKey)["AVGPRICE"].agg(["first"])
print("FIRST ITEM : ",asd1)
print("")
#마지막 아이템
asd2 = dtfma.groupby(by=groupKey)["AVGPRICE"].agg(["last"])
print("last item : ",asd2)
print("")
#평균값
asd3 = dtfma.groupby(by=groupKey)["AVGPRICE"].agg(["mean"])
print("average : ",asd3)
print("")
#중간값
asd4 = dtfma.groupby(by=groupKey)["AVGPRICE"].agg(["median"])
print("middle value : ",asd4)
print("")
#최소값
asd5 = dtfma.groupby(by=groupKey)["AVGPRICE"].agg(["min"])
print("min value : ",asd5)
print("")
#최대값
asd6 = dtfma.groupby(by=groupKey)["AVGPRICE"].agg(["max"])
print("max value : ",asd6)
print("")
#표준편차
asd7 = dtfma.groupby(by=groupKey)["AVGPRICE"].agg(["std"])
print("asd7 : ",asd7)
print("")
#분산
asd8 = dtfma.groupby(by=groupKey)["AVGPRICE"].agg(["var"])
print("asd8 : ",asd8)
print("")
#그룹데이터의곱
asd9 = dtfma.groupby(by=groupKey)["AVGPRICE"].agg(["prod"])
print("all * : ",asd9)
print("")
#그룹데이터의합
asd10 = dtfma.groupby(by=groupKey)["AVGPRICE"].agg(["sum"])
print("sum : ",asd10)
print("")
#사분위수
asd11 = dtfma.groupby(by=groupKey)["AVGPRICE"].agg(["quantile"])
print("asd11 : ", asd11)



--------------------
#실습
import pandas as pd
import numpy as np

mydatafm = pd.read_csv("./dataset/kopo_channel_seasonality_new.csv")
mydatafm = mydatafm.astype({'QTY':'int64'})
print(mydatafm)
print(mydatafm.dtypes)
#불량데이터처리
#QTY컬럼이 음수면 0, 양수면 기존값 유지
mydatafm["QTY_NEW"] = np.where(mydatafm.QTY < 0, 0, mydatafm.QTY)

print("")
#반박코드문
print(mydatafm[mydatafm["QTY_NEW"] < 0])
#실행결과 = empty

mydatafm = mydatafm.astype({'YEARWEEK':'str'})
mydatafm['YEAR'] = mydatafm.YEARWEEK.str[:4]
mydatafm['WEEK'] = mydatafm.YEARWEEK.str[4:]
mydatafm = mydatafm.astype( {'YEAR' : 'int64'})
mydatafm = mydatafm.astype( {'WEEK' : 'int64'})
print(mydatafm.dtypes)
print("")
mydatafm = mydatafm[mydatafm['WEEK'] < 53]
mydatafm = mydatafm.astype({'WEEK' : 'str'})
mydatafm['WEEK']=mydatafm['WEEK'].apply(lambda x : str(x).zfill(2))
# replyfm = mydatafm[["REGIONID", "PRODUCT", "YEARWEEK", "QTY_NEW"]]
# print(replyfm)
# print("")
grKey = ["REGIONID", "PRODUCT", "YEARWEEK"]
grpfm = mydatafm.sort_values(by=grKey)
print(grpfm)
print("")

grkey2 = ["REGIONID", "PRODUCT", "YEAR"]
gr2fm = mydatafm.groupby(by=grkey2)["QTY_NEW"].agg(['mean'])
gr2fm = gr2fm.reset_index()
print(gr2fm)
gr2fm = gr2fm.rename(columns={'QTY_NEW':'QTY_MEAN'})
print(gr2fm)

# import pandas as pd
# from sqlalchemy import create_engine
# import pymysql

# pymysql.install_as_MySQLdb()
# #mysql 연결 엔진 생성
# engine = create_engine("mysql+pymysql://kopo:kopo"+"@192.168.110.111/kopo", encoding='utf-8')
# conn = engine.connect() #엔진을 시작
# #cvs파일을 읽어와서 dataframe을 이용해서 저장

# #dataframe을 sql에 테이블 자동으로 생성해서 넣어준다.
# replyfm.to_sql(name='customer_data_jewooklee1', con=engine, if_exists='append', index=False)

# #테이블 생성및 insert가 완료되었는지 확인하는 sql조회문
# indata=pd.read_sql_query("select * from customer_data_jewooklee1", engine)
# print(indata)
