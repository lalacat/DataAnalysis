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

# data 碧云东方公寓 3室2厅 142_66平米(1200)
# spilt






data='''
碧云东方公寓 3室2厅 142_66平米(1200)  
凤凰大厦 1室1厅 80_35平米(356)  
百富丽山庄 6室3厅 342平米(1810)	 
金浦小区(金桥) --室--厅 66_66平米(280)	 
'''




# data_list = data.strip().split(' ')
# print(data_list)
text="foo bar \t baz  \tqux"

import re
# a = re.split('\s+',data)
# b = re.split('\s+',text)

# print(a)
# print(b)

# regex = re.compile('\s+')
# regex = re.compile('\s+')
regex = re.compile('碧云东方公寓')
regex_01 = re.compile('3+')
# print(regex.findall(text))
# print(regex_01.findall(data))

m =regex.findall(data)
print(m)

