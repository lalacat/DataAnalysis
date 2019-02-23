import pymongo,collections

# mongodb服务的地址和端口号
mongo_url = "127.0.0.1:27017"
# mongo_port = 27017

# 连接到mongodb，如果参数不填，默认为“localhost:27017”
client = pymongo.MongoClient(mongo_url)

#连接到数据库myDatabase
DATABASE = "PuDong_Sold"
db = client[DATABASE]

coll = db['Task_caolu']



# 阿里云地址
Ali_url = '47.105.165.81:27017'

# data = coll.find({},{'_id':0})
#
#
# new_database = collections.defaultdict(list)
#
# while True:
#     try:
#         temp = data.next()
#         if len(temp) > 2:
#             temp.pop('community_name')
#             for name,info in temp.items():
#                 new_database['community_name'].append(name)
#                 new_database['sold_address'].append(info['sold_address'])
#                 new_database['sold_dealDate'].append(info['sold_dealDate'])
#                 new_database['sold_dealcycle'].append(info['sold_dealcycle'])
#                 new_database['sold_house_url'].append(info['sold_house_url'])
#                 new_database['sold_positionInfo'].append(info['sold_positionInfo'])
#
#     except StopIteration:
#         break

def conver_data(coll):
    data = coll.find({}, {'_id': 0})
    new_database = collections.defaultdict(list)

    while True:
        try:
            temp = data.next()
            if len(temp) > 2:
                temp.pop('community_name')
                for name, info in temp.items():
                    new_database['community_name'].append(name)
                    new_database['sold_address'].append(info['sold_address'])
                    new_database['sold_dealDate'].append(info['sold_dealDate'])
                    new_database['sold_dealcycle'].append(info['sold_dealcycle'])
                    new_database['sold_house_url'].append(info['sold_house_url'])
                    new_database['sold_positionInfo'].append(info['sold_positionInfo'])

        except StopIteration:
            break




