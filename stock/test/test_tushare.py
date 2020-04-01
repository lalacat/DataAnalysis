import tushare as ts
import pandas as pd
import datetime as dt
import matplotlib.pyplot as plt
token = 'bfbf67e56f47ef62e570fc6595d57909f9fc516d3749458e2eb6186a'

ts_code = '002192.SZ'
startday = '20190326'
endday= '20190328'
pro = ts.pro_api(token)


df = pro.daily(ts_code=ts_code, start_date=startday, end_date=endday)

for index,i in df.iterrows():
    print(i['close'])
# datas = pd.date_range('2019-03-26','2019-03-28')
# df['time'] = datas
# 分时数据

# df = ts.get_tick_data('002192',date='2019-04-18',src='tt')
# print(df['time'])
# print(df['price'][df['time']>dt.datetime(2019,4,19,10,0,0)])
t = '2019-4-18 14:56:42'
# t = dt.datetime.strptime('20190531','%Y%m%d')

# print(type(t))
n_t= dt.datetime.strptime(t,'%Y-%m-%d %H:%M:%S')
if(n_t < dt.datetime(2019,4,19,10,0,0)):
    print('true')