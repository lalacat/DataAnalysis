
# file_base_path = 'C:\\华泰\\工作\\data\\cffex\\{0}\\{1}.csv'
# 字符串转换日期格式
import csv
from collections import defaultdict
from datetime import timedelta, datetime

from chinese_calendar import is_holiday
import pandas as pd

class import_cffex(object):
    def __init__(self):
        self.company_name = ['华泰期货','中信期货','海通期货','上海东证']
        # self.company_name = ['上海东证']
        self.result = {}
        self.number = 1
        self.total_result = defaultdict(list)

    def get_tradingday(self,start_day,end_day):
        start_week = start_day.isoweekday()
        days = []
        end = False
        # global number
        for day in range(6-start_week):
            t = start_day+timedelta(days=day)
            if t == end_day:
                end = True
                day =  6 - start_week - 1
            if t.isoweekday() < 6:
                if not is_holiday(t):
                    days.append(t)
            if day == 6 - start_week - 1:
                if days:
                    self.result[str(self.number)] = days
                    self.number = self.number + 1
                if end:
                    break
                next_weekday = t + timedelta(days=3)
                self.get_tradingday(next_weekday,end_day)

    def get_company_data(self,csvfilepath):
        date = csvfilepath.split('\\')[-1].split('.')[0]
        with open(csvfilepath, 'r', newline='', encoding='gb18030') as csvfile:
            reader = csv.reader(csvfile)  # 创建csv.reader对象
            total_num = {}
            for row in reader:
                for name in self.company_name:
                    if name == row[3]:
                        num = total_num.get(name, 0)
                        total_num[name] = num + int(row[4])
            for name in self.company_name:
                if not total_num.get(name, None):
                    total_num[name] = 0

                self.total_result[name].append([date,total_num[name]])

    def clear_data(self):
        self.total_result.clear()


start = datetime.strptime('20200101','%Y%m%d').date()
end_day = datetime.strptime('20200430','%Y%m%d').date()
cf = import_cffex()
cf.get_tradingday(start,end_day)
file_base_path = 'C:\\华泰\\工作\\data\\cffex\\{0}\\{1}.csv'
result_path = 'C:\\华泰\\工作\\data\\cffex\\{0}\\{1}.csv'
sorts = ['IF_1','IC_1','IH_1','TS_1','TF_1','T_1']
for s in sorts:
    for i in range(1,len(cf.result)+1):
        week = cf.result[str(i)]
        for day in week:
            day_temp = day.strftime('%Y%m%d')
            print('%s:%s 正在处理'%(s,day_temp))
            if day_temp in ['20200131']:
                continue
            file_name= file_base_path.format(s,day_temp)
            cf.get_company_data(file_name)

    for name,values in cf.total_result.items():
        file_name =  'C:\\华泰\\工作\\data\\cffex\\result\\{1}_{0}.csv'.format(s,name)
        first_line = []
        # print(len(values))

        with open(file_name,'w',newline='') as f:
            f_csv = csv.writer(f)
            if not first_line:
                f_csv.writerow(['date',s])
            f_csv.writerows(values)

        print('%s：已处理' %file_name.split('\\')[-1])

    cf.clear_data()
