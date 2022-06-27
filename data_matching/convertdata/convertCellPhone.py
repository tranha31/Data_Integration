import json
import base64

f_listPhone = open("../data/cellphone.json", "r", encoding="utf-8-sig")
listPhone = json.load(f_listPhone)

f_listPhone.close()

data = []

for i in range(0, len(listPhone)):
    item = listPhone[i]
    dicData = {}
    dicData["name"] = item.get("name")
    dicData["memory"] = item.get("memory")
    dicData["operating_system"] = item.get("operating_system")
    dicData["pin"] = item.get("pin")
    dicData["price"] = item.get("price")
    dicData["ram"] = item.get("ram")
    dicData["screen"] = item.get("screen")
    dicData["sim"] = item.get("sim")
    dicData["front_camera"] = item.get("front_camera")
    dicData["behind_camera"] = item.get("behind_camera")
    dicData["chip"] = item.get("chip")
    dicData["color"] = item.get("color")
    dicData["image_url"] = str(base64.b64decode(item["image_url"]["$binary"]["base64"]))[2:-1]
    dicData["url"] = str(base64.b64decode(item["url"]["$binary"]["base64"]))[2:-1]

    data.append(dicData)

with open('data_cell.json', 'w', encoding='utf-8') as f:
    json.dump(data, f, ensure_ascii=False, indent=4)

