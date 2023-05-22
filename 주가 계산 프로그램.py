import FinanceDataReader as web
from datetime import date, timedelta
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker
#폰트 때문에 사용함
import platform

from matplotlib import font_manager, rc
if platform.system() == 'Windows':
    font_name = font_manager.FontProperties(fname="c:/Windows/Fonts/malgun.ttf").get_name()
    rc('font', family=font_name)
elif platform.system() == 'Darwin':
    rc('font', family='AppleGothic')
else:
    pass

today = date.today()
startday = date.today() - timedelta(720) #timedelta 사용해서 자동으로 빼준다.
yesterday = date.today() - timedelta(1)
print(yesterday)

#SEC value에 크롤링한 데이터들이 담긴다.
SEC = web.DataReader("207940", startday, yesterday)
print(type(SEC))
print(SEC.tail(10))
SEC['Close'].plot(figsize=(16,4))

DEC = web.DataReader("USD/KRW", startday, yesterday)
#DEC['Close'].plot(figsize=(16,4))

BTC = web.DataReader("BTC/KRW", startday, yesterday)
#print(BTC)
# config = {
#     'width' : 800,
#     'height' : 600,
#     'volume' : True,
# }

# web.chart.config(config=config)
# web.chart.plot(SEC, title='SAMSUNGG')

# 2행으로 쪼갠다 // 컬럼1개 // 그중에 첫번째 라는뜻
plt.subplot(411)
plt.title("Price Chart")
plt.ylim([600000, 1100000])     # Y축의 범위: [ymin, ymax]
plt.gca().yaxis.set_major_formatter(mticker.FormatStrFormatter('%d'))

SEC[str(startday):str(yesterday)]['Close'].plot(figsize=(16,10), style='b',xlabel='Date', ylabel='종가')
#SEC["2020-05-06":"2022-05-06"]['Close'].plot(figsize=(16,10), style='b',xlabel='Date', ylabel='종가')
plt.subplots_adjust(hspace=0.5)

# 2행으로 쪼갠것 중에 컬럼 1개의 두번째.
plt.subplot(412)
SEC[str(startday):str(yesterday)]["Volume"].plot(figsize=(16,10), style='b',xlabel='Date',ylabel='볼륨')
#SEC["2020-05-06":"2022-05-06"]["Volume"].plot(figsize=(16,10), style='g')

plt.subplot(413)
DEC[str(startday):str(yesterday)]['Close'].plot(figsize=(16,10), style='b',xlabel='Date',ylabel='환율가격')

plt.subplot(414)
BTC[str(startday):str(yesterday)]['Volume'].plot(figsize=(16,10), style='b',xlabel='Date',ylabel='코인가격')

plt.show()
