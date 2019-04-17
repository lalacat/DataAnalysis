import datetime as dt
import pandas

import mpl_finance as mpf
import matplotlib.dates as dts
import pandas_datareader as web
import matplotlib.pyplot as plt
import tushare as ts
import matplotlib as mpl

# start = (2018,1,1)
# end = (2019,3,28)
# quotes = web.DataReader('300450.SZ',data_source='yahoo',start='3/01/2018',end='3/26/2019')
# print(quotes)
# cols = list(quotes)

# fig,ax = plt.subplots(figsize=(8,5))
# fig.subplots_adjust(bottom=0.2)
# mpf.candlestick_ochl(ax,quotes)
# cols.insert(0,cols.pop(cols.index('date')))
# # cols.pop(cols.index('Adj Close'))
# new_quotes = quotes.ix[:, cols[0:5]]
#




token = 'bfbf67e56f47ef62e570fc6595d57909f9fc516d3749458e2eb6186a'

ts_code = '002192.SZ'
startday = '20190101'
endday= '20190415'
pro = ts.pro_api(token)

# 获取数据
quotes = pro.daily(ts_code=ts_code, start_date=startday, end_date=endday)
# print(colms)
# 按照时间序列升序
result = quotes.sort_values(by='trade_date', ascending=True)


# 转换时间序列, DatetimeIndex 转换为 float
def conver_time(time):
    t = pandas.date_range(time,periods=1)
    return mpl.dates.date2num(t.to_pydatetime())[0]


result['trade_date'] = result['trade_date'].apply(lambda x:conver_time(x))

data = result.loc[len(result.index):,['trade_date','open','close','high','low']]
# datas.columns=['','','','','']
datas = data.values
# print(datas)
# 画图
fig,ax = plt.subplots(figsize=(8,5))
fig.subplots_adjust(bottom=0.2)
# # mpf.candlestick2_ochl(ax,result['open'],result['close'],result['high'],result['low'],width=1,colorup='r',colordown='b')
mpf.candlestick_ochl(ax,datas)
ax.xaxis_date()
ax.autoscale_view()
plt.grid(True)
plt.show()


