import json
from operator import itemgetter
from pkgutil import iter_modules
from tkinter.tix import Tree

f_listPhone = open("../data/fphone.json", "r", encoding="utf-8-sig")
listPhone = json.load(f_listPhone)

f_listPhone.close()

dicColor = {
    "Xanh dương": "Blue",
    "Xanh lá" : "Green",
    "Xanh" : "Blue",
    "Xám" : "Grey",
    "Đỏ" : "Red",
    "Vàng" : "Gold",
    "Cam" : "Orange",
    "Tím" : "Violet",
    "Bạc" : "Sliver",
    "Đen" : "Black",
    "Trắng" : "White",
    "Hồng" : "Pink",
    "Đồng" : "Copper"
}

data = []
lstKey = list(dicColor.keys())
for i in range(len(listPhone)):
    item = listPhone[i]
    
    if(item["ROM"] == None or "mb" in item["ROM"].lower()):
        continue

    item["price"] = int(item["price"])
    if item["price"] == 0:
        item["price"] = None

    if item["ROM"] != None:
        if("gb" in item["ROM"].lower() or "tb" in item["ROM"].lower()):
            item["ROM"] = int((item["ROM"].strip())[0:-2])
        else:
            item["ROM"] = None
        
        if item["ROM"] != None and item["ROM"] < 10:
            item["ROM"] = item["ROM"] * 1024
    
    if item["RAM"] != None:
        item["RAM"] = item["RAM"][0:5].replace('+','').replace(' ', '')
        if("gb" in item["RAM"].lower()):
            item["RAM"] = int((item["RAM"].strip())[0:-2])
        else:
            item["RAM"] = int((item["RAM"].strip()))

    item["color"] = dicColor.get(item["color"].strip())

    # item["name"] = item["name"].replace("Điện Thoại Di Động", "")
    # item["name"] = item["name"].replace("(Hết bảo hành)", "")
    # item["name"] = item["name"].replace("- Hàng trưng bày", "")
    # item["name"] = item["name"].strip()

    data.append(item)

with open('data_fpt.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)