import os
import re
from collections import defaultdict, OrderedDict
from pprint import pprint
import shutil
import pandas as pd

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
filters_01 = ['短视频', 'SFC-PR', 'Tokyo','pondo','系列-FC']
filters_02 = ['系列-FC','系列-Caribbean']
filter_file_01 = re.compile('|'.join(filters_01))
filter_file_02 = re.compile('|'.join(filters_02))
all_type = ['wmv', 'torrent', 'mp4', 'jpg', 'mkv', 'gif', 'db', 'jpeg', 'td', 'apk', 'exe', 'avi', 'rmvb', 'MP4', 'png',
            'html', 'rtf',
            'vtt', 'srt', 'chm', 'mht', 'JPG', 'AVI', 'htm', 'url', 'zip', 'rar']
del_type = ['gif', 'db', 'td', 'apk', 'exe', 'html', 'rtf', 'vtt', 'srt', 'chm', 'mht', 'htm', 'url', 'zip', 'rar']

file_type = list(set(all_type) - set(del_type))

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
        self.del_types = ['gif', 'db', 'td', 'apk', 'exe', 'html', 'rtf', 'vtt', 'srt', 'chm', 'mht', 'htm', 'url',
                          'zip', 'rar']
        self.result = OrderedDict([])
        self.del_dirs = set()
        self.temp_dirs = []
        self.temp_files = []

    def scand_file_filters(self, path):
        with os.scandir(path) as all_files:
            for file in all_files:
                if not filter_file_01.match(file.name):
                    if not re.match('系列',file.name):
                        for root, dirs, files in os.walk(file.path):
                            # 处理系列之外的文件
                            # 当前目录地址
                            # print(root)
                            # # 获取当前目录下的文件夹

                            dir_name = root.split('\\')[-1]
                            base_path = ''.join(list(root)[:-len(dir_name)])
                            dir_name,mov_name, actor_name, c_flag = self.deal_dir_name(dir_name,base_path)
                            torrent_flag = None
                            mov_flag = None
                            appendix = None
                            if len(files) >0:
                                try:
                                    for f in files:
                                        # name = f.split('.')[0]
                                        type = f.split('.')[-1]
                                        if type == 'torrent':
                                            torrent_flag = type
                                        elif type in ['wmv', 'mp4', 'mkv', 'avi', 'rmvb', 'MP4', 'AVI']:
                                            if not mov_flag:
                                                mov_flag = f
                                            else:
                                                mov_flag = ',' + f
                                        else:
                                            if appendix:
                                                appendix = ',' + f
                                            else:
                                                appendix = f
                                except IndexError:
                                    print('test')
                            self.result[mov_name]=[actor_name,c_flag,mov_flag,torrent_flag,appendix]
                    else:
                        # 处理系列内的文件
                        with os.scandir(file.path) as series_files:
                            for dir in series_files:
                                if not re.match(filter_file_02,dir.name):
                                    scan_dirs_flag = True
                                    scan_files_flag = False
                                    for root, dirs, files in os.walk(dir.path):
                                        print(root)
                                        if scan_dirs_flag:
                                            files_num = len(dirs)
                                            base_path = root
                                            scan_dirs_flag = False
                                            result = {}
                                        else:
                                            scan_files_flag = True
                                        if scan_files_flag:
                                            # print(files)
                                            torrent_flag = None
                                            mov_flag = None
                                            appendix = None
                                            dir_name = root.split('\\')[-1]
                                            dir_name, mov_name, actor_name, c_flag = self.deal_dir_name(
                                                dir_name, base_path)
                                            for f in files:
                                                type = f.split('.')[-1]
                                                if type == 'torrent':
                                                    torrent_flag = type
                                                elif type in ['wmv', 'mp4', 'mkv', 'avi', 'rmvb', 'MP4', 'AVI']:
                                                    if not mov_flag:
                                                        mov_flag = f
                                                    else:
                                                        mov_flag = ',' + f
                                                else:
                                                    if appendix:
                                                        appendix = ',' + f
                                                    else:
                                                        appendix = f
                                            self.result[mov_name] = [actor_name, c_flag, mov_flag, torrent_flag, appendix]
                                            # result[mov_name] = [actor_name, c_flag, mov_flag, torrent_flag, appendix]
                                            files_num -= 1
                                            if files_num == 0:
                                                # print(result)
                                                # print('=============')
                                                scan_dirs_flag = True
                                                scan_files_flag = False

                                        """
                                        if len(dirs) > 0:
                                            if len(self.temp_dirs) == 0:
                                                self.temp_dirs = dirs
                                                print(root)
                                                base_path = root
                                            if len(self.temp_files) >0:
                                                torrent_flag = None
                                                mov_flag = None
                                                appendix = None
                                                for i in range(len(self.temp_dirs)):
                                                    dir_name = self.temp_dirs[i]
                                                    # base_path = temp_root
                                                    dir_name, mov_name, actor_name, c_flag = self.deal_dir_name(
                                                        dir_name, base_path)
                                                    for f in self.temp_files[i]:
                                                        type = f.split('.')[-1]
                                                        if type == 'torrent':
                                                            torrent_flag = type
                                                        elif type in ['wmv', 'mp4', 'mkv', 'avi', 'rmvb', 'MP4', 'AVI']:
                                                            if not mov_flag:
                                                                mov_flag = f
                                                            else:
                                                                mov_flag = ',' + f
                                                        else:
                                                            if appendix:
                                                                appendix = ',' + f
                                                            else:
                                                                appendix = f

                                                    self.result[mov_name] = [actor_name, c_flag, mov_flag, torrent_flag,
                                                                             appendix]
                                                    torrent_flag = None
                                                    mov_flag = None
                                                    appendix = None
                                                    # print(self.result)
                                            self.temp_dirs = dirs
                                            base_path = root
                                            self.temp_files = list()
                                        self.temp_files.append(files)
                                    """


    def deal_dir_name(self,dir_name,base_path):
        c_flag = None
        C_end = re.match('^\w{1,}(-\w{1,})?-\d{2,}-[CZS]', dir_name)  # -C/Z
        two_blank = re.match('.*[0-9]{3,}\s{2}', dir_name)
        litter_letter = re.match('[a-z]{1,}-[0-9]{3,}',dir_name)
        if C_end:
            c_flag = 1
        if two_blank:
            new_name = ' '.join([i for i in dir_name.split(' ') if i != ''])
            old_path = os.path.join(base_path,dir_name)
            new_path = os.path.join(base_path, new_name)

            os.rename(old_path, new_path)
            print('%s 改名为 %s' % (dir_name, new_name))
            dir_name = new_name
        if litter_letter:
            old_path = os.path.join(base_path, dir_name)
            new_path = os.path.join(base_path, dir_name.upper())
            # os.rename(old_path, new_path)
            print('%s 改名为 %s' % (old_path, new_path))

        # 处理文件夹名
        name = dir_name.split(' ')
        if len(name) > 1:
            actor_name = ' '.join(name[1:])
        else:
            actor_name = 0
        mov_name = name[0]

        return dir_name,mov_name,actor_name,c_flag

    def scand_file_all(self,path):
        for root, dirs, files in os.walk(path):
            if len(files) > 0:
                for f in files:
                    path = os.path.join(root, f)
                    self.all_types = self.get_type(f)
                    self.del_filepath(f, path)

    def del_no_need_dirs(self,path):
        with os.scandir(path) as all_files:
            for file in all_files:
                if not filter_file_01.match(file.name):
                    with os.scandir(file.path) as series_files:
                        for dir in series_files:
                            if not re.match(filter_file_02, dir.name):
                                for root, dirs, files in os.walk(dir.path):
                                    if len(dirs) > 0:
                                        for d in dirs:
                                            if not re.match('^\w{1,}-\d{3,}', d):
                                                del_dirpath = os.path.join(root, d)
                                                up_dirs = del_dirpath.split('\\')
                                                if not re.match('^\w{1,}-\d{3,}', up_dirs[-2]):
                                                    new_path = del_dirpath[:-len(up_dirs[-1])-1]
                                                else:
                                                    new_path = del_dirpath
                                                self.del_dirs.add(new_path)
                        for d_d in self.del_dirs:
                            shutil.rmtree(d_d)
                            print('%s 已删除' % d_d)


    # 处理文件
    # 获得所有的文件格式
    def get_type(self, file):
        type = file.split('.')[-1]
        if type not in all_type:
            all_type.append(type)
        return all_type

    # 删除某类格式的文件
    def del_filepath(self, file,path: str):
        # if os.path.exists(path):  # 如果文件存在
        type = file.split('.')[-1]
        if type in self.del_types:
            # 删除文件
            # os.remove(path)
            print('%s 已删除' % path)
        # else:
        #     print('no such file:%s' % path)


fd = FileDeal()
fd.scand_file_filters(path)
final = pd.DataFrame(fd.result,index=['actor_name','c_flag','mov','torrent_flag','appendix']).swapaxes(0,1)
final.to_excel('E:\\备份\\movie_list.xlsx')
# print(final)


# 日文编码 [\u0800-\u4e00]
# 中文编码 [\u4e00-\u9fa5]
# pattern1 = '^[cC]arib'  # Carib
# pattern2 = '.*[0-9]{3,}$'  # 数字结尾
# pattern3 = '.*[0-9]{3,}\s{2}'  # 2个空格
# # pattern4 = '^\d?\w{1,}-.*[0-9]{3,}(?=-[A-Za-z])'  # 匹配-字母的
# pattern4 = '^\d?\w{1,}([-_]\d{3,})+(?=-[A-Za-z])'  # 匹配-字母的
# pattern5 = '^[^A-Za-z0-9]'  # 非字母数字开头
# pattern6 = '^\d?\w{1,}([-_]\d{3,})+[_-]\d{3,}\S'  #

# 强制删除，文件夹不为空也不报错
# shutil.rmtree('C:\\Users\\scott\\Desktop\\spacesniffer_1_3_0_2\\test')
# os.removedirs('C:\\Users\\scott\\Desktop\\spacesniffer_1_3_0_2\\test')

#
# test = OrderedDict([])
# test['a'] = [1,2,3,5]
# test['b'] = [4,6,7,8]
# data = pd.DataFrame(test,index=['c_flag','actor name','mov','appendix'])
# print(data.swapaxes(0,1))