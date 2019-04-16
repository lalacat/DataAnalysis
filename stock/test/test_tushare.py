import tushare as ts
import pandas as pd
import matplotlib.pyplot as plt
token = 'bfbf67e56f47ef62e570fc6595d57909f9fc516d3749458e2eb6186a'

ts_code = '002192.SZ'
startday = '20190326'
endday= '20190328'
pro = ts.pro_api(token)


df = pro.daily(ts_code=ts_code, start_date=startday, end_date=endday)
datas = pd.date_range('2019-03-26','2019-03-28')
df['time'] = datas
print(df)
# datas = pd.DataFrame(df)
# # datas[['open','close']].plot()
# plt.plot(datas['trade_date'],datas[['open','close']])
# plt.gcf().autofmt_xdate()
# plt.show()
