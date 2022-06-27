import json
from pkgutil import iter_modules
from traceback import print_tb

from torch import le

f_listPhone = open("./data/fphone.json", "r", encoding="utf-8-sig")
listPhone = json.load(f_listPhone)

f_listPhone.close()

data = []

for i in range(0, len(listPhone)):
    item = listPhone[i]
    if type(item) == list:
        phone = item[0]
        for j in range(0, len(phone["variants"])):
            itemP = phone["variants"][j]
            dicData = {}
            dicData["name"] = phone.get("name")
            dicData["release_date"] = phone.get("release_date")
            dicData["sim_card"] = phone.get("sim_card")
            dicData["CPU"] = phone.get("CPU")
            dicData["RAM"] = phone.get("RAM")
            dicData["ROM"] = phone.get("ROM")
            dicData["battery"] = phone.get("battery")
            dicData["battery_type"] = phone.get("battery_type")
            dicData["brand"] = phone.get("brand")
            dicData["display"] = phone.get("display")
            dicData["display_resolution"] = phone.get("display_resolution")
            dicData["display_size"] = phone.get("display_size")
            dicData["color"] = itemP["color"]
            dicData["price"] = itemP["price"]
            dicData["price_market"] = itemP["price_market"]
            dicData["variant_image"] = itemP["variant_image"]

            data.append(dicData)
    else:
        for j in range(0, len(item["variants"])):
            itemP = item["variants"][j]
            dicData = {}
            dicData["name"] = item.get("name")
            dicData["release_date"] = item.get("release_date")
            dicData["sim_card"] = item.get("sim_card")
            dicData["CPU"] = item.get("CPU")
            dicData["RAM"] = item.get("RAM")
            dicData["ROM"] = item.get("ROM")
            dicData["battery"] = item.get("battery")
            dicData["battery_type"] = item.get("battery_type")
            dicData["brand"] = item.get("brand")
            dicData["display"] = item.get("display")
            dicData["display_resolution"] = item.get("display_resolution")
            dicData["display_size"] = item.get("display_size")
            dicData["color"] = itemP["color"]
            dicData["price"] = itemP["price"]
            dicData["price_market"] = itemP["price_market"]
            dicData["variant_image"] = itemP["variant_image"]

            data.append(dicData)
    

with open('data.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)
