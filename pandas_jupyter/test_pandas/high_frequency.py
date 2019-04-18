import tushare as ts
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
token = 'bfbf67e56f47ef62e570fc6595d57909f9fc516d3749458e2eb6186a'

# 获取时间
day = '2019-04-18'
# 获取历史分时行情
df = ts.get_tick_data('002192',date='2019-04-18',src='tt')
# 添加上交易日
df['time'] = day+' '+df['time']
# 转换为datetime格式，用于筛选时间段

df.index = df['time'].apply(lambda t: dt.datetime.strptime(t,'%Y-%m-%d %H:%M:%S'))

# print(df['price'][(df.index >dt.datetime(2019,4,18,10,35,0)) & (df.index <dt.datetime(2019,4,18,11,30,0))])
rule = (df.index >=dt.datetime(2019,4,18,9,30,0)) & (df.index <=dt.datetime(2019,4,18,11,30,0))|\
       (df.index >=dt.datetime(2019,4,18,13,00,0))& (df.index <=dt.datetime(2019,4,18,15,00,0))
# df['price'][rule].plot(style='b',figsize=(8,5))
# plt.show()

print(df['price'])