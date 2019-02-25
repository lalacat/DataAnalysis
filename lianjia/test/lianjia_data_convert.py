import pymongo,collections

# mongodb服务的地址和端口号
mongo_url = "127.0.0.1:27017"
# mongo_port = 27017

# 连接到mongodb，如果参数不填，默认为“localhost:27017”
local_client = pymongo.MongoClient(mongo_url)

#连接到数据库myDatabase
local_dbbase = "PuDong_Sold"
local_db = local_client[local_dbbase]

local_coll = local_db['Task_caolu']

# 阿里云地址
Ali_url = '47.105.165.81:27170'
Ali_dbbase = 'LianJia'
Ali_client = pymongo.MongoClient(Ali_url)
Ali_db = Ali_client[Ali_dbbase]
Ali_db.authenticate('test','test123')
Ali_coll = Ali_db['caolu']



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
        except KeyError:
            print(temp)

    return new_database


# cd = conver_data(local_coll)
# Ali_coll.insert(cd)
all_name = local_db.list_collection_names()

print(len(all_name))
for old_name in all_name:
    if old_name != 'ErrUrl':
        new_name = old_name.split('_')[-1]
        # if old_name != 'Task_caolu':
        local_coll = local_db[old_name]
        c_d = conver_data(local_coll)
        ali_coll = Ali_db[new_name]
        ali_coll.insert(c_d)
        print('%s finish' %old_name)


# remove
# new_name = Ali_db.list_collection_names()
# print(len(new_name))
# for name in new_name:
#     Ali_db.drop_collection(name)