import cx_Oracle
username = 'marketdata'
password = 'marketdata'
tns = 'marketdata:marketdata/HQDB2'
conn = cx_Oracle.connect(username,password,tns)
cursor = conn.cursor()