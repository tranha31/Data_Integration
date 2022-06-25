import pymongo
from os.path import dirname, abspath
import json
client = pymongo.MongoClient("mongodb://localhost:27017/")
client.get_database('fpt_phone')
client.drop_database('fpt_phone')
db = client['fpt_phone']
phone, variants = db['phone'], db['variants']
path = dirname(abspath(__file__))
with open(path+'\\fphone.json', encoding='utf8') as f:
    content = f.read()
    data = json.loads(content)
for i in data:    
    _variants = i['variants']
    i.pop('variants')
    id = phone.insert_one(i).inserted_id
    for v in _variants:
        v['phone_id'] = id
        variants.insert_one(v)
def get_joined_items():
    joined_items = db.phone.aggregate([
        

        {"$lookup": {
        "from": "variants",
        "localField": "_id",
        "foreignField": "phone_id",
        "as": "variants"
        }},
        {"$unwind": "$variants"}
        ])
    return joined_items
    
#items = get_joined_items()
#for i in items:
#    print(i)
#    break