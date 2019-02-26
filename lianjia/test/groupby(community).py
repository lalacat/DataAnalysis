import pymongo
import pandas as pd
Ali_url = '47.105.165.81:27170'
Ali_dbbase = 'LianJia'
Ali_client = pymongo.MongoClient(Ali_url)
Ali_db = Ali_client[Ali_dbbase]
Ali_db.authenticate('test','test123')
Ali_coll = Ali_db['biyun']
data = Ali_coll.find({},{'_id':0}).next()

deal_data = pd.DataFrame(data)
#
# info = deal_data.info()
# print(info)
# print(deal_data.describe())


# print(deal_data['sold_totalPrice'].head(45))

def deal_num(str_num):
    try:
        num_type = type(eval(str_num))

        if num_type == int:
            # print('int')
            return int(str_num)
        elif num_type == float:
            return float(str_num)
        else:
            raise SyntaxError
    except SyntaxError:
        return None
# community_name
# sold_address
# sold_dealDate
# sold_totalPrice
# sold_unitPrice
# sold_dealcycle
# sold_saleonborad
# sold_positionInfo
def house_type(community_name):
    pass