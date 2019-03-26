import numpy as np
import pandas as pd
import pandas_datareader as web
import matplotlib.pyplot as plt

XD = web.DataReader('300450.SZ',data_source='yahoo',start='7/28/2017',end='3/26/2019')
# XD['5d'] = np.round(pd.rolling_mean(XD['Close'],window=5),2)
XD['5d'] = np.round(XD['Close'].rolling(5).mean(),2)
XD['20d'] = np.round(XD['Close'].rolling(20).mean(),2)
a = XD[['Close','5d','20d']].plot(grid=True,figsize=(8,5))
plt.show()