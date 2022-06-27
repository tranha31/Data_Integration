import json
from pkgutil import iter_modules

f_listPhone = open("../data/cellphone.json", "r", encoding="utf-8-sig")
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
    "Hồng" : "Pink"
}

data = []
for i in range(len(listPhone)):
    item = listPhone[i]
    if(item["memory"] == None or "mb" in item["memory"].lower()):
        continue

    if item["price"][0:3] == "Giá":
        item["price"] = None
    else:
        item["price"] = int(item["price"].replace('.', '').strip())
    if item["memory"] != None:
        if("gb" in item["memory"].lower() or "tb" in item["memory"].lower()):
            item["memory"] = int((item["memory"].strip())[0:-3])
        else:
            item["memory"] = int((item["memory"].strip()))
        
        if item["memory"] < 10:
            item["memory"] = item["memory"] * 1024
    
    if item["ram"] != None:
        item["ram"] = item["ram"][0:5].replace('+','').replace(' ', '')
        if("gb" in item["ram"].lower()):
            item["ram"] = int((item["ram"].strip())[0:-2])
        else:
            item["ram"] = int((item["ram"].strip()))
    item["color"] = dicColor.get(item["color"].strip())
    item["name"] = item["name"].replace("| Chính hãng VN/A", "")
    item["name"] = item["name"].replace("I Chính hãng VN/A", "")
    item["name"] = item["name"].strip()

    data.append(item)

with open('data_cell.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)