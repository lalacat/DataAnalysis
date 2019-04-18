import pandas as pd
from urllib.request import urlretrieve
import  statsmodels.api as sm
# 下载数据
# es_url = "https://www.stoxx.com/document/Indices/Current/HistoricalData/hbrbcpe.txt"
# vs_url = 'https://www.stoxx.com/document/Indices/Current/HistoricalData/h_vstoxx.txt'
#
# urlretrieve(es_url,'./data/es.txt')
# urlretrieve(vs_url,'./data/vs.txt')

# lines = open('./data/es.txt','r').readlines()
# lines = [line.replace(' ','') for line in lines]

# print(lines)
# new_file = open('./data/es50.txt','w')
# new_file.writelines('data'+lines[3][:-1]+';DEL'+lines[3][-1])
# new_file.writelines(lines[4:])
# new_file.close()

# a = ';SX5P;SX5E;SXXP;SXXE;SXXF;SXXA;DK5F;DKXF\n'
# print(a[:-1])