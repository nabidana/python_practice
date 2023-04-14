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
