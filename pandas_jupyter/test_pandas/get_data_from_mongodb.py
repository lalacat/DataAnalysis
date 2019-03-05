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

data = coll.find({},{'_id':0})

import_data = data.next()
import_data.pop('community_name')

# print(pprint.pformat(import_data))
frame = pd.DataFrame(import_data)

frame_T = frame.T
del frame_T['sold_house_url']
# del frame_T['sold_house_url']
# del frame_T['sold_house_url']

# print(frame_T.columns)
print(frame_T)