import os
import pprint
import re
from collections import defaultdict

import xlrd
import xlwt

path = 'Z:\\每日备份\\201805-201812'
filter_mounths  = ['201810','201811','201812']


class GetHostInfo(object):

    def __init__(self):
        pass


    def find_excel(self,paths,filter_mounths=None):
        if not isinstance(paths,list):
            raise TypeError('路径是list类型')
        results = dict()
        files_is_none = list()
        for path in paths:
            if os.path.isfile(path):
                print('is file')
                pass
            else:
                with os.scandir(path) as all_mounth_files:
                    for mounth_file in all_mounth_files:
                        if mounth_file.name in filter_mounths:
                            with os.scandir(mounth_file.path) as all_day_files:

                                for day_file in all_day_files:
                                    if day_file.is_dir():
                                        hostDir = day_file.path + '\\ASP7\\工作日志'
                                        hostFilePath = self.check_file_excel(hostDir)
                                        if hostFilePath:
                                            results[day_file.name] = hostFilePath
                                        else:
                                            results[day_file.name] = 0
                                            files_is_none.append(day_file.name)
                                    else:
                                        name = re.search('.*?(\d{8})\.xls',day_file.name).group(1)
                                        results[name] = day_file.path
                                for f in files_is_none:
                                    keys  = list(sorted(results.keys()))
                                    f_n = keys.index(f)
                                    new_f_n = f_n - 3
                                    if new_f_n < len(keys):
                                        results[f] = results[keys[new_f_n]]
                                    else:

                                        new_f_n = f_n + 3
                                        results[f] = results[keys[new_f_n]]
                return results


    def getResults(self,path):
        pass

    def check_file_excel(self,path):
        with os.scandir(path) as final_file:
            for hostFile in final_file:
                if hostFile.name.endswith('.xls'):
                    return hostFile.path
            return False

    def get_data_from_excle(data,excle_file_path):
        result = dict()
        with xlrd.open_workbook(excle_file_path) as wb:
            sheet2 = wb.sheet_by_name('Sheet2')
            sheet3 = wb.sheet_by_name('Sheet3')

            result['shfe1'] = sheet2.cell(6,10).value
            result['cffex1'] = sheet2.cell(21,10).value

            result['shfe2'] = sheet3.cell(6,10).value
            result['cffex2'] = sheet3.cell(21,10).value


        return result

    def write_into_excel(self,date):
        wbk = xlwt.Workbook()
        sheet = wbk.add_sheet('Sheet1')
        i = 0
        for k,v in date.items():
            try:
                sheet.write(i,0,k)
                sheet.write(i,1,v['shfe1'])
                sheet.write(i,2,v['cffex1'])
                sheet.write(i,3,v['shfe2'])
                sheet.write(i,4,v['cffex2'])
                i += 1
            except Exception as e :
                print(e)
        wbk.save('C:\\华泰\\工作\\季度报告\\2019年第一季度\\import_host.xls')


path2 = 'Z:\\每日备份\操作平台日志'
ghi = GetHostInfo()
data = ghi.find_excel([path2],['201901','201902','201903'])
res = defaultdict(dict)
for name,path in data.items():
    res[name] = ghi.get_data_from_excle(path)

ghi.write_into_excel(res)

# print(pprint.pformat(res))
# # name = re.search('.*?(\d{8})\.xls','综合交易平台值班日志20181008.xls').group(1)
# # print(name)