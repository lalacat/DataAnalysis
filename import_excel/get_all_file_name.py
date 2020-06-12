import os
import re
from collections import defaultdict
from pprint import pprint

path = 'E:\\备份\\电影'
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
filters = ['短视频','SFC-PR','系列-FC2','Carib','Tokyo']
filter_file  = re.compile('|'.join(filters))
all_type = ['wmv', 'torrent', 'mp4', 'jpg', 'mkv', 'gif', 'db', 'jpeg', 'td', 'apk', 'exe', 'avi', 'rmvb', 'MP4', 'png', 'html', 'rtf',
            'vtt', 'srt', 'chm', 'mht', 'JPG', 'AVI', 'htm', 'url', 'zip', 'rar']
del_type = ['gif', 'db','td', 'apk', 'exe','html', 'rtf','vtt', 'srt', 'chm', 'mht','htm', 'url', 'zip', 'rar']

file_type = list(set(all_type)-set(del_type))

# print(file_type)
del_path = []
# a = filter_file.search(path).group()
# print(a)
# b = filter_file.findall(path3)
# print(b)

class FileDeal(object):

    def __init__(self):
        self.all_types = list()
        self.del_files = list()
        self.del_types = ['gif', 'db','td', 'apk', 'exe','html', 'rtf','vtt', 'srt', 'chm', 'mht','htm', 'url', 'zip', 'rar']

    def scand_all_file(self,path):
        with os.scandir(path) as all_day_files:
            for day_file in all_day_files:
                if filter_file.match(day_file.name):
                    continue
                for root,dirs,files in os.walk(day_file.path):
                    # 当前目录地址
                    # print(root)
                    # # 获取当前目录下的文件夹
                    # print(dirs)
                    # # 获取当前目录下的所有文件
                    if len(files) > 0:
                        dir_name = root.split('\\')[-1]
                        print(dir_name)
                        # 处理文件夹名

                        # type = f.split('.')[-1]
                        # if type not in all_type:
                        #     all_type.append(type)
                        for f in files:
                            # path =
                            self.all_types = self.get_type(f)
                            self.del_types(f)
                        # if type in del_type:
                        #     p = os.path.join(root, f)
                        #     # del_path.append(os.path.join(root, f))
                        #     os.remove(p)
                        #     print('%s 已删除'%p)


                                # print(files)
                        # print('--------------------------')
                    #     result[day_file.name].append(files)
                    # if re

    # 处理文件
    # 获得所有的文件格式
    def get_type(self,file):
        type = file.split('.')[-1]
        if type not in all_type:
            all_type.append(type)
        return all_type

    # 删除某类格式的文件
    def del_filepath(self,file:str):
        # if os.path.exists(path):  # 如果文件存在
        type = file.split('.')[-1]
        if type in self.del_types:
            # 删除文件
            # os.remove(path)
            print('%s 已删除' % path)
        # else:
        #     print('no such file:%s' % path)
# fd = FileDeal()
# fd.scand_all_file(path)
# print(result)
# print(all_type)
# print(pprint(del_path))

str1 = 'Carib-012017-355'
str2 = 'Carib-082917-488-FHD'
str3 = 'Caribbean-120614-753慟哭の女教師_前編_～だらしなく砕け散るプライド～大橋未久'
str4 ='Caribbean-122015-050 放課後に、仕込んでください ～おじさんといる方が楽しいし～ 碧木凛［avziyuan.net］'
strs = [
    str1,str2,str3,str4,
    'グラマラス 立花瑠莉 122318_786-1pon-1080p',#
    '080114_01-10mu-whole1_hd', #需要过滤的数字开头
    '230orec-473-C', # 数字开头 + 小写
    '259LUXU-1093',# 数字开头
    'jufe-102 佐知子',# 小写字母
    'pondo-071213_625いい旅_卑猥な気分_伊藤美侑佳',#没有空格+日文
    'RHJ-311  尾野真知子',#两个空格
    'ADN-031.本田岬.去からの悪しき訪問者 夫を愛しているのに、私は…。 本田岬',#-C结尾
    'HEYZO 0763 宅配女僕讓附近迷惑的絶叫性愛 吉村美咲[無碼中文字幕]',#没有-
    'IBW-722Z',#z或者c结尾的
]
# 日文编码 [\u0800-\u4e00]
# 中文编码 [\u4e00-\u9fa5]
pattern1 = '^[cC]arib' # Carib
pattern2 = '.*[0-9]{3,}$' # 数字结尾
pattern3 = '.*[0-9]{3,}\s{0,2}' # 2 个空格
pattern4 = '.*-[0-9]{3}[^\s]'


for s in strs:

    # if re.match(pattern1,s):
    #     print('Carib匹配: %s' %s)
    if re.search(pattern2,s):
        pass
        # print("日文(中文)无空格匹配：%s" %s)
        # c = re.match(pattern2, s).span()[1]
        # old = list(s)
        # old.insert(c,' ')
        # new = ''.join(old)
        # print("修改后：%s" %new)
    else:
        if re.match(pattern4,s):
            print(s)
        # if re.search(pattern4, s):
        #     print(s)

