import collections
import pprint

import pymongo
import pandas


# 阿里云地址
Ali_url = '47.105.165.81:27170'
Ali_dbbase = 'LianJia'
Ali_client = pymongo.MongoClient(Ali_url)
Ali_db = Ali_client[Ali_dbbase]
Ali_db.authenticate('test','test123')
Ali_coll = Ali_db['biyun']


data = Ali_coll.find({},{'_id':0})
# print(pprint.pformat(data.next()))
pd_data = pandas.DataFrame(data.next())
print(pd_data.head(1))