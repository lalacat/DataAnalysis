import numpy
import pandas as pd
import matplotlib.pyplot as plt

df = pd.DataFrame([10,20,30,40],columns=['numbers'],index=['a','b','c','d'])
df['floats'] = (1.3,2.1,3.4,5.6)
df['name'] = pd.DataFrame(['bibi','lili','pipi','qiqi'],index=['d','a','b','c'])
df = df.append(pd.DataFrame({'name':'jiji','floats':'8.9','numbers':60},index=['z']))
# print(df)

# 生成正态分布
a = numpy.random.standard_normal((9,4))
df_01 = pd.DataFrame(a)
# 生成时间序列
dates = pd.date_range('20190101',periods=9,freq='M')
# print(dates)
df_01.index = dates
# print(df_01)

# # 总和
# print(df_01.sum())
# # 平均值
# print(df_01.mean())
# # 累积和
# print(df_01.cumsum())
# 数值数据统计
# print(df_01.describe())

# df_01.cumsum().plot(lw=2.0)
# plt.show()
df_01.columns=[['NO1','NO2','NO3','NO4']]
# print(df_01)
# print(df_01['NO1'])
df_01['NO1'].cumsum().plot(style='r',lw=2.0)
plt.show()