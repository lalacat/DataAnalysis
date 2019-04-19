import tushare as ts
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt

import matplotlib.dates as mdates
import matplotlib.ticker as ticker

token = 'bfbf67e56f47ef62e570fc6595d57909f9fc516d3749458e2eb6186a'

# 获取时间
# day = '2019-04-18'
# 获取历史分时行情
# df = ts.get_tick_data('002192',date='2019-04-18',src='tt')
# 添加上交易日
# df['time'] = day+' '+df['time']
# 转换为datetime格式，用于筛选时间段
# df.index = df['time'].apply(lambda t: dt.datetime.strptime(t,'%Y-%m-%d %H:%M:%S'))
# df['price'].plot(style='b',lw=1.5)
# print(df.index)

# 读一周的分时数据
''''''
RJ_data = pd.DataFrame()
for i in ['15','16','17','18','19']:
    day = '2019-04-'+i
    df = ts.get_tick_data('002192', date=day, src='tt')
    df['time'] = day+' '+df['time']
    df['time'] = df['time'].apply(lambda t: dt.datetime.strptime(t, '%Y-%m-%d %H:%M:%S'))
    # print(df.info())
    if len(RJ_data) == 0:
        RJ_data = df
    else:
        # RJ_data.append(df[['time','price',  'change',  'volume',   'amount', 'type']])
        RJ_data = RJ_data.append(df,ignore_index=True)


print(RJ_data.head())
# RJ_data.index = RJ_data['time']
# RJ_data['price'].plot(style='b')

# plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
# plt.gca().xaxis.set_major_locator(mdates.DayLocator())

# 画图
# fig,ax1 = plt.subplots()
# plt.plot(RJ_data['volume'],'b',lw=1.5)
# # 设置x轴的标签，用时间显示
# ax1.set_xticklabels(RJ_data['time'])
# plt.setp(plt.gca().get_xticklabels(),rotation=30,horizontalalignment='right')
# # 与上一句等价
# """
# for label in ax.get_xticklabels():
#     label.set_rotation(30)
#     label.set_horizontalalignment('right')
# """
#
# ax2 = ax1.twinx()
# plt.plot(RJ_data['price'],'r',lw=1.5)
#
#
#
#
# plt.show()