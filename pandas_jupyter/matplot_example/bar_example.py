import datetime as dt

import mpl_finance as mpf
import matplotlib.dates as dts
import pandas_datareader as web
import matplotlib.pyplot as plt
import tushare as ts
import matplotlib.pyplot as plt

# start = (2018,1,1)
# end = (2019,3,28)
# quotes = web.DataReader('300450.SZ',data_source='yahoo',start='3/01/2018',end='3/26/2019')
# print(quotes.index)
# timeRecord = dts.date2num(quotes.index)
# quotes['date'] = timeRecord
# cols = list(quotes)

# cols.insert(0,cols.pop(cols.index('date')))
# # cols.pop(cols.index('Adj Close'))
# new_quotes = quotes.ix[:, cols[0:5]]
#
# result = [( t, open, close, high, low) for  t, open, close, high, low in new_quotes.values]



token = 'bfbf67e56f47ef62e570fc6595d57909f9fc516d3749458e2eb6186a'

ts_code = '002192.SZ'
startday = '20190326'
endday= '20190328'
pro = ts.pro_api(token)

quotes = pro.daily(ts_code=ts_code, start_date=startday, end_date=endday)
colms = list(quotes)
print(colms)
# print(quotes['trade_date'])
def str2date(str_dates):
    result = list()
    for str_date in str_dates:
        print(str_date)
        a = dt.datetime.strptime(str_date[0:4]+'-'+str_date[4:6]+'-'+str_date[6:],'%Y-%m-%d')
        result.append(a)
    return result

date =str2date(quotes['trade_date'].str)
timeRecord = dts.date2num(date)
print(timeRecord)

# fig,ax = plt.subplots(figsize=(8,5))
# fig.subplots_adjust(bottom=0.2)
# mpf.candlestick_ochl(ax,result,width=1,colorup='r',colordown='b')
# ax.xaxis_date()
# # ax.autoscale_view()
# plt.grid(True)
# plt.show()
#

