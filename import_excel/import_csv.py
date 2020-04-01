import os
import re
import csv
from collections import defaultdict
import time

class find_id(object):

    def __init__(self):
        self.result = defaultdict(list)
        self.filter_files = [
        ]
        self.investid = [
            '16000530',
            '10901393',
            '13300228',
            '16000362',
            '11802727',
            '11001077',
            '16000530',
            '16000530'
        ]
    def find_csv(self,path):
        dirs = os.listdir(path)
        results = []
        for file_name in dirs:
            if 'csv' in file_name:
                if self.filter_files:
                    if file_name  not in self.filter_files:
                        file_name = path+'\\' +file_name
                        results.append(file_name)
                else:
                    file_name = path + '\\' + file_name
                    results.append(file_name)

        return results


    def read_csv(self,csvfilepath):#列表方式读取
        print(csvfilepath)
        with open(csvfilepath, 'r', newline='',encoding='gb18030') as csvfile:
            reader = csv.reader(csvfile)#创建csv.reader对象
            first_row = None
            name = csvfilepath.split('\\')[-1]
            result = []
            for row in reader:
                if not first_row:
                    first_row = row
                    result.append(first_row)
                    continue
                # 读取出的内容是列表格式的
                if name == 't_InstrumentCommissionRate.csv':
                    # print(int(row[1]))
                    if int(row[1]) != 3:
                        result.append(row)
                for id in self.investid:
                    if id in row:
                      result.append(row)

            if len(result) > 1:
                self.result[name]=result

    def writer_csv(self,path):
        print('===========写入')
        if self.result:
            for name,info in self.result.items():
                file_path = path+'\\'+name
                print(file_path)
                with open(file_path,'w',newline='') as f:
                    f_csv = csv.writer(f)
                    f_csv.writerows(info)

    def copy_csv(self,path):
        src = path + '\\'


if __name__== '__main__':
    fi = find_id()
    perf_path= 'C:\\华泰\\perf\\2xperf'
    # perf_path = 'C:\华泰\perf\perf'
    r = fi.find_csv(perf_path)
    start_time = time.process_time()
    for i in r:
        fi.readcsv(i)

    print(time.process_time()-start_time)
    # print(fi.result)
    write_path = perf_path+'\\new'
    fi.writecsv(write_path)
