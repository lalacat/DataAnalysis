
import mpl_finance as mpf
import pandas_datareader as web
import matplotlib.pyplot as plt
start = (2018,1,1)
end = (2019,3,28)

quotes = web.DataReader('300450.SZ',data_source='yahoo',start='3/01/2018',end='3/26/2019')
# print(quotes.index)
fig,ax = plt.subplots(figsize=(8,5))
fig.subplots_adjust(bottom=0.2)
mpf.candlestick2_ochl(ax,quotes['Open'],quotes['Close'],quotes['High'],quotes['Low'],width=1,
                      colorup='b',colordown='r')

ax.autoscale_view()
plt.grid(True)
plt.show()