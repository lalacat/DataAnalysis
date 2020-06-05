import os
import re
from collections import defaultdict
path = 'Z:\\每日备份\\201912'
def find_file(path):
    with os.scandir(path) as all_day_files:
        for day_file in all_day_files:
            print(day_file)
            if day_file.is_dir():
                with os.scandir(day_file.path) as all_files:
                    for files in all_files:
                        print(files)
            # if mounth_file.name in filter_mounths:
            #     with os.scandir(mounth_file.path) as all_day_files:
            #
            #         for day_file in all_day_files:
            #             if day_file.is_dir():
            #                 hostDir = day_file.path + '\\ASP7\\工作日志'
            #                 hostFilePath = self.check_file_excel(hostDir)
            #                 if hostFilePath:
            #                     results[day_file.name] = hostFilePath
            #                 else:
            #                     results[day_file.name] = 0
            #                     files_is_none.append(day_file.name)
            #             else:
            #                 name = re.search('.*?(\d{8})\.xls', day_file.name).group(1)
            #                 results[name] = day_file.path




# find_file(path)
result = defaultdict(list)
filter_file  = re.compile(r"\\?ASP")
path = 'Z:\\每日备份\\201912\\20191216\\ASP7'
path2 ="""
Z:\每日备份\201912\20191216
['ASP7']
Z:\每日备份\201912\20191216\ASP7
['check.txt', '委托', '客户结算单', '工作日志', '报单响应时间统计', '报单响应时间统计2', '报送文件', '数据库增量备份', '流水(flow和syslog)', '用户事件', '系统监控记录', '行情文件', '银期流水']
Z:\每日备份\201912\20191216\ASP7\check.txt
[]
"""

a = filter_file.search(path).group()
print(a)
b = filter_file.search(path2,re.S).group()
print(b)
# with os.scandir(path) as all_day_files:
#     # print(all_day_files)
#     for day_file in all_day_files:
#         # print(day_file)
#         # print(day_file.path)
#         for root,dirs,files in os.walk(day_file.path):
#             # 当前目录地址
#             print(root)
#             # # 获取当前目录下的文件夹
#             print(dirs)
#             # # 获取当前目录下的所有文件
#             # print(files)
#             # print('--------------------------')
#             if len(files) > 0:
#                 result[day_file.name].append(files)
#             # if re
#         print('%s finished' %day_file.name)
#         if day_file.is_dir():
#             with os.scandir(day_file.path) as all_files:
#                 for files in all_files:
#                     print(files)
# for root, dirs, files in os.walk(path):
#     print(root)
#     print(dirs)
#     print(files)
    # for file in files:
    #     # 获取文件所属目录
    #     # print(root)
    #     # 获取文件路径
    #     print(os.path.join(root, file))

# print(result)