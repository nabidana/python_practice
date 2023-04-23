import pandas as pd
import numpy as np

people_project = pd.read_csv('./Pythonfd/test1/사원.csv', encoding='cp949')
print(people_project)

group_project = pd.read_csv('./Pythonfd/test1/부서.csv', encoding='cp949')
print(group_project)

jobplace_project = pd.read_csv('./Pythonfd/test1/직급.csv', encoding='cp949')
print(jobplace_project)

address_project = pd.read_csv('./Pythonfd/test1/근무지.csv', encoding='cp949')
print(address_project)

# 1. 급여가 800만원 이상인 사원의 사원명, 직급코드를 출력하시오
test1_project = people_project
test1_project=test1_project[test1_project['급여']>8000000]
test1_project=test1_project[['사원명','직급코드']]
print(test1_project)

# 2. 입사일이 2010년~2018년 사이인 사원의 사원명, 부서코드, 급여, 입사일을 출력하시오
test2_project = people_project
test2_project['date'] = test2_project.입사일.str[:4]
#데이터값이 NaN인거 전부 제거하기 > dataframe.dropna()
#특정 컬럼값이 NaN인거 제거하기
test2_project = test2_project.dropna(subset= ['사원명'])
test2_project = test2_project.astype({'date' : 'int'})
test2_project = test2_project[ (test2_project['date'] >= 2012) & (test2_project['date'] <=2018)]
#이상하게 test2를 건들였는데 원본인 people에 date컬럼이 추가되어있다.
people_project = people_project.drop( labels='date', axis=1)
test2_project = test2_project[['사원명','부서코드','급여','입사일']]
print(test2_project)

# 3. 입사일이 2020년 08월이면서 부서코드가 'C'가 아닌 사원의 사원명, 근무지코드, 부서코드를 출력하시오
test3_project = people_project
test3_project['date'] = test3_project.입사일.str[:4]+test3_project.입사일.str[5:7]
test2_project = test2_project.dropna(subset= ['사원명'])
test3_project = test3_project[ (test3_project['date'] != '202008')& (test3_project['부서코드'] !='C')]
people_project = people_project.drop(labels='date', axis=1)
test3_project = test3_project[ ['사원명', '근무지코드', '부서코드']]
print(test3_project)
print("")

# 4. 사원의 총인원수를 출력하시오
test4_project = people_project
test4_project = test4_project.dropna(subset=['사원명'])
test4_count = len(test4_project)
print(test4_count)
print("")

# 5. 상급자사원번호가 없는 사원의 총인원수와 총급여합을  출력하시오
test5_project = people_project
test5_project = test5_project.dropna(subset=['사원명'])
test5_project = test5_project[ test5_project['상급자사원번호'].isnull()]
test5_peoplecount = len(test5_project)
test5_totalpay = test5_project['급여'].sum()
print(test5_peoplecount)
print(test5_totalpay)
print("")

# 6. 급여가 300만원이하이면서 2020년 08월 15일 이후에 입사한 사원의 총인원수와 총급여합을 출력하시오
test6_project = people_project
test6_project = test6_project.dropna(subset=['사원명'])
test6_project['date'] = test6_project.입사일.str[:4]+test6_project.입사일.str[5:7]+test6_project.입사일.str[8:10]
test6_project = test6_project.astype({'date' : 'int'})
test6_project = test6_project[ (test6_project['date'] > 20200815) & (test6_project['급여'] < 3000000)]
test6_count = len(test6_project)
test6_total = test6_project['급여'].sum()
print(test6_count)
print(test6_total)
print("")

# 7. '한' 씨 성을 가진 사원들을 출력하시오
test7_project = people_project
test7_project = test7_project.dropna(subset=['사원명'])
# '한' 글자로 시작하는거 찾기
test7_project = test7_project[test7_project['사원명'].str.startswith('한')]
#test7_project = test7_project[ test7_project['사원명'].str[0] == '한']
print(test7_project)
print("")

# 8. 직급별 급여의 평균을 출력하시오(반올림해서 정수만 출력)
test8_project = people_project
test8_project = test8_project[ ['직급코드', '급여']]
# mean > 평균구하기 // round : 반올림
test8_project = test8_project.groupby('직급코드').mean().round(0)
test8_project = test8_project.astype({'급여' : 'int'})
print(test8_project)
print("")

# 9. 사원명에 '삭' 자가 포함되어 있거나 '김'씨 성을 가진 사원의 급여합을 출력하시오
test9_project = people_project
test9_project = test9_project.dropna(subset=['사원명'])
#str.contains > 특정 문자 검색
test9_project = test9_project[test9_project.사원명.str.contains('김|삭')]
print(test9_project)
print("")

# 10. 부서별 사원수를 출력하시오
test10_project = people_project
test10_project = test10_project[ ['부서코드', '사원명']]
test10_project = test10_project.groupby('부서코드').count()
#rename : 컬럼명 변경하기
test10_project = test10_project.rename(columns={ '사원명' : '사원수'})
print(test10_project)
print("")

# 11. 근무지별 사원의 총인원수를 출력하시오
test11_project = people_project
test11_project = test11_project[ ['근무지코드', '사원명']]
test11_project = test11_project.groupby('근무지코드').count()
test11_project = test11_project.rename(columns={ '사원명' : '사원수'})
print(test11_project)
print("")

# 12. 가장 높은 급여와 가장 낮은 급여를 출력하시오
test12_project = people_project
test12_maxcount = test12_project['급여'].max()
test12_mincount = test12_project['급여'].min()
print(test12_maxcount)
print(test12_mincount)
print("")

# 13. 급여가 500만원 이상, 800만원 이하인 사원의 급여평균과 급여의 최대값을 출력하시오
test13_project = people_project
test13_project = test13_project.dropna(subset=['사원명'])
test13_project = test13_project[ (test13_project['급여'] >= 5000000) & (test13_project['급여'] <= 8000000)]
test13_meancount = round(test13_project.급여.mean())
test13_maxcount = test13_project['급여'].max()
print(test13_meancount)
print(test13_maxcount)
print("")

# 14. 가장 높은 급여와 가장 낮은 급여의 차를 출력하시오
test14_count = test12_maxcount - test12_mincount
print(test14_count)
print("")

# 15. 근무지가 'A1'이 아닌 사원들의 부서코드별 사원수를 출력하시오
test15_project = people_project
test15_project = test15_project.dropna(subset=['사원명'])
test15_project = test15_project[ test15_project['근무지코드'] != 'A1']
test15_project = test15_project[ ['부서코드', '사원명']]
test15_project = test15_project.rename(columns={ '사원명' : '사원수'})
test15_project = test15_project.groupby('부서코드').count()
print(test15_project)
print("")

# 16. 부서코드별 사원번호순으로 부서코드, 사원번호, 사원명, 급여의 누적값을 구해서 출력하시오
test16_project = people_project
test16_project = test16_project.dropna(subset=['사원명'])
test16_project = test16_project.sort_values( ['사원번호', '부서코드'])
test16_project = test16_project[ ['부서코드', '급여']]
test16_project = test16_project.groupby('부서코드').sum()
print(test16_project)
print("")

# 17. 부서명, 사원명 출력하시오 
test17_project = people_project
test17_group = group_project
test17_project = test17_project.dropna(subset=['사원명'])
test17_project = pd.merge(left=test17_project, right=test17_group, how = "outer", on="부서코드")
test17_project = test17_project[ ['사원명', '부서명']]
print(test17_project)
print("")
