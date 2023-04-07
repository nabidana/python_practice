#1. mysql 연결
import pandas as pd
from sqlalchemy import create_engine
import pymysql


pymysql.install_as_MySQLdb()
#mysql 연결 엔진 생성
engine = create_engine("mysql+pymysql://kopo:kopo"+"@192.168.110.111/kopo", encoding='utf-8')
conn = engine.connect() #엔진을 시작
#cvs파일을 읽어와서 dataframe을 이용해서 저장
testData = pd.read_csv("./dataset/customerdata.csv")
print(testData)
#dataframe을 sql에 테이블 자동으로 생성해서 넣어준다.
testData.to_sql(name='customer_jewooklee', con=engine, if_exists='append', index=False)

#테이블 생성및 insert가 완료되었는지 확인하는 sql조회문
indata=pd.read_sql_query("select * from customer_jewooklee", engine)
print(indata)

#2. 포스트sql
import psycopg2
import pandas as pd
from sqlalchemy import create_engine 
# csv 데이터 로딩 후 컬럼 소문자로 변환
selloutData = pd.read_csv("../dataset/kopo_product_volume.csv")
#selloutData.columns = ["regionid","productgroup","yearweek","volume"]
print(selloutData)
# 데이터베이스 접속 엔진 생성
engine = create_engine('postgresql://postgres:postgres@127.0.0.1:5432/postgres') 
# 데이터 저장
resultname='kopo_product_volume'
selloutData.to_sql(name=resultname, con=engine, index = False, if_exists='replace’)
# 데이터 불러오기
indata = pd.read_sql_query("select * from kopo_product_volume", engine)
print(indata)
                   
                   
