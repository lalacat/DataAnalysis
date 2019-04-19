import pandas_datareader as web
import matplotlib.pyplot as plt
import tushare as ts
import numpy as np

a = np.array([1,2,3])
print(type(a))



# tushare
# web.DataReader
# 读取融捷股份的数据
# RJ = web.DataReader('300450.SZ',data_source='yahoo',start='3/01/2015')
# print(RJ.info())
# print(RJ.tail())
# 画图

# RJ['Close'].plot(figsize=(8,5))
# # 单个对数收益率
# plt.show()
token = 'bfbf67e56f47ef62e570fc6595d57909f9fc516d3749458e2eb6186a'

ts_code = '002192.SZ'
startday = '20150101'
endday= '20190417'
pro = ts.pro_api(token)

# 获取数据
RJ = pro.daily(ts_code=ts_code, start_date=startday, end_date=endday)
# print(RJ.info())
print(RJ['trade_date'][RJ['vol']>100000])