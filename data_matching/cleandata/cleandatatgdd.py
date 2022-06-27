import json
from pkgutil import iter_modules

f_listPhone = open("../data/tgdd.json", "r", encoding="utf-8-sig")
listPhone = json.load(f_listPhone)

f_listPhone.close()

dicColor = {
    "xanh dương": "Blue",
    "xanh lá" : "Green",
    "xanh" : "Blue",
    "xám" : "Grey",
    "đỏ" : "Red",
    "vàng" : "Gold",
    "cam" : "Orange",
    "tím" : "Violet",
    "bạc" : "Sliver",
    "đen" : "Black",
    "trắng" : "White",
    "hồng" : "Pink",
    "xanh lam" : "Blue",
    "xanh ngọc" : "Blue",
    "đen nhãn" : "Black",
}

data = []
for i in range(len(listPhone)):
    item = listPhone[i]
    
    if item["Ram"] != None:
        item["Ram"] = item["Ram"][0:5].replace('+','').replace(' ', '')
        if("gb" in item["Ram"].lower()):
            item["Ram"] = int((item["Ram"].strip())[0:-2])
        else:
            item["Ram"] = int((item["Ram"].strip()))
    if item["Color"] != None:
        item["Color"] = dicColor.get(item["Color"].strip().lower())
    

    data.append(item)

with open('data_tgdd.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)