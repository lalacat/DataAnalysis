import pandas_datareader as web
import matplotlib.pyplot as plt

# tushare
# web.DataReader
# 读取融捷股份的数据
RJ = web.DataReader('300450.SZ',data_source='yahoo',start='3/01/2015')
# print(RJ.info())
# print(RJ.tail())
# 画图

RJ['Close'].plot(figsize=(8,5))
# 单个对数收益率
plt.show()
