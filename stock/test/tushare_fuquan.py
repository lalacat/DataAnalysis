import tushare as ts
# import pandas as pd
import datetime as dt
# import matplotlib.pyplot as plt
token = 'bfbf67e56f47ef62e570fc6595d57909f9fc516d3749458e2eb6186a'

ts_code = '002192.SZ'
startday = '20190326'
endday= '20190328'
# pro = ts.pro_api(token)

ts.set_token(token)
# df = pro.daily(ts_code=ts_code, start_date=startday, end_date=endday)

df = ts.pro_bar(ts_code=ts_code,asset='E', adj='qfq', start_date=startday, end_date=endday)
df_after = ts.pro_bar(ts_code=ts_code,asset='E', start_date=startday, end_date=endday)

# print(df)
# print(df_after)
t1 = dt.datetime.now()
print(dt.datetime.strftime(t1,'%Y%m%d'))