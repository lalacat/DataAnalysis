import pymongo
import pandas as pd
import pprint

mongo_url = "127.0.0.1:27017"
# mongo_port = 27017

# 连接到mongodb，如果参数不填，默认为“localhost:27017”
client = pymongo.MongoClient(mongo_url)

#连接到数据库myDatabase
DATABASE = "PuDong_Sold"
db = client[DATABASE]

coll = db['Task_anshan']

data = coll.find({},{'_id':0,'community_name':0})

import_data = data.next()
# import_data.pop('community_name')

frame = pd.DataFrame(import_data)
# 返回 行标签
# print(frame.index)

frame.drop(['sold_address','sold_house_url'],inplace=True)
print(frame)

# frame_T = frame.T
# frame_T_drop = frame_T.drop(['sold_address','sold_dealcycle'],axis=1)
#
# print(frame_T_drop)