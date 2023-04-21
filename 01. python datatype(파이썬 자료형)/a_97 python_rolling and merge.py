#Rolling함수는 이전 특정 범위의 행값을 이용해서 평균을 구하는 함수이다
# 사용법

#자신의 이전 숫자들을 가지고 평균을 구할 경우
dataframe['컬럼명'].rolling(window=숫자).mean()
# 여기서 .mean()은 평균을 구하는 것이다

#하지만 만약 숫자가 10처럼 큰숫자가 들어갈경우 0~9번인덱스까지는 값이 표시가 되지 않는다.
#따라서 자신을 중심으로 위, 아래의 값들을 가지고 평균을 구하고 싶을 경우에는
dataframe['컬럼명'].rolling(window=숫자, center=True).mean()
#을 사용하면 된다.
#최소 구간을 설정하여서 범위에 해당안되는값으 잇더라도, 제외하고 계산하고싶을 경우에는
dataframe['컬럼명'].rolling(window=숫자, center=True, min_periods=숫자).mean()
#을 아용하면 된다.

import pandas as pd
import numpy as np

joms = pd.read_csv('../dataset/join_region_master.csv', encoding='ms949')
josl = pd.read_csv('../dataset/join_kopo_product_volume.csv')

#merge는 두개의 다른 컬럼을 구룹바이처럼 하나의 카테고리를 기준으ㅗㄹ 합치는 것.
qwe = pd.merge(left = josl, right=joms, on = ['REGIONID'])
print(qwe)

#컬럼의 이름을 바꾸는것
josl = josl.rename(columns={"REGIONID":"SALESID"})
#merge에서 속성값을 참조할경우
asd = pd.merge ( left= josl, right=joms, left_on="SALESID", right_on= "REGIONID")\
            [ ['REGIONID', 'REGIONNAME', 'PRODUCT', "QTY"] ]

print(asd)

