import pymongo
import pandas

# mongodb服务的地址和端口号
mongo_url = "127.0.0.1:27017"
# mongo_port = 27017

# 连接到mongodb，如果参数不填，默认为“localhost:27017”
client = pymongo.MongoClient(mongo_url)

#连接到数据库myDatabase
DATABASE = "PuDong_Sold"
db = client[DATABASE]

coll = db['Task_caolu']

# data = coll.find({})
# print(data.count())
# while True:
#     try:
#         print(data.next())
#     except StopIteration:
#         break

data = pandas.DataFrame(list(coll.find({})))
data.fillna(value=0)


# 删除mongodb中的_id字段
del data['_id']
for i in data.head(5):
    # l = len(i)
    # print(str(l)+str(i))
    print(type(i))
    # for j in i :
    #     print(j)
    # print(i)