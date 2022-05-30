from matplotlib.font_manager import json_dump
from dl import DL
import json
import re

oDL = DL()

# Hàm này để lưu dữ liệu lần đầu crawl vào db ạ
def saveData():
    f_listPhone1 = open('../phone1_tgdd.json', 'r', encoding='utf-8-sig')
    f_listPhone = open('../phone_tgdd.json', 'r', encoding='utf-8-sig')

    listPhone1 = json.load(f_listPhone1)
    listPhone = json.load(f_listPhone)
    beforeSaveData(listPhone1)
    beforeSaveData(listPhone)

    f_listPhone1.close()
    f_listPhone.close()


# Lọc dữ liệu không dùng + chuẩn hóa lại dữ liệu
def beforeSaveData(listItem):
    for item in listItem:
        if (item["company"].lower() == "masstel") or (item["company"].lower() == "nokia" and re.search("^Nokia +[0-9]", item["name"])) or (item["company"].lower() == "itel" and re.search("^Itel it", item["name"])):
            continue
        if("gb" in item["memory"].lower()):
            item["memory"] = int((item["memory"].strip())[0:-3])
        else:
            item["memory"] = int((item["memory"].strip()))
        
        index = item["originPrice"].index("₫")
        item["originPrice"] = int(item["originPrice"][0: index].replace('.', '').strip())
        if item["discountRate"] != None:
            index = item["discountRate"].index("%")
            item["discountRate"] = float(item["discountRate"][0: index].strip())
        if item["discountPrice"] != None:
            index = item["discountPrice"].index("₫")
            item["discountPrice"] = int(item["discountPrice"][0: index].replace('.', '').strip())

        for i in range(len(item["imageUrl"])):
            data = []
            data.append(item["company"])
            data.append(item["name"])
            data.append(item["memory"])
            if(i < len(item["color"])):
                data.append(item["color"][i])
            else:
                data.append(None)
            data.append(item["originPrice"])
            data.append(item["discountPrice"])
            data.append(item["discountRate"])
            data.append(item["screen"])
            data.append(item["operatingSystem"])
            data.append(item["frontCamera"])
            data.append(item["behindCamera"])
            data.append(item["chip"])
            data.append(item["ram"])
            data.append(item["sim"])
            data.append(item["pin"])
            data.append(item["imageUrl"][i])

            oDL.Insert(tuple(data))

# Hàm này là để check trùng lặp, để biết là thêm mới hay update thông tin
def updateData():
    phone = oDL.GetAll()
    f_listPhone1 = open('../phone1_tgdd.json', 'r', encoding='utf-8-sig')
    f_listPhone = open('../phone_tgdd.json', 'r', encoding='utf-8-sig')

    listPhone1 = json.load(f_listPhone1)
    listPhone = json.load(f_listPhone)
    for item in listPhone1:
        checkDuplicate(item, phone)
    
    for item in listPhone:
        checkDuplicate(item, phone)

    f_listPhone1.close()
    f_listPhone.close()

def checkDuplicate(item, lstPhone):
    if("gb" in item["memory"].lower()):
            item["memory"] = int((item["memory"].strip())[0:-3])
    else:
        item["memory"] = int((item["memory"].strip()))
    index = item["originPrice"].index("₫")
    item["originPrice"] = int(item["originPrice"][0: index].replace('.', '').strip())
    if item["discountRate"] != None:
        index = item["discountRate"].index("%")
        item["discountRate"] = float(item["discountRate"][0: index].strip())
    if item["discountPrice"] != None:
        index = item["discountPrice"].index("₫")
        item["discountPrice"] = int(item["discountPrice"][0: index].replace('.', '').strip())
    for i in range(len(item["imageUrl"])):
        data = []
        data.append(item["company"])
        data.append(item["name"])
        data.append(item["memory"])
        if(i < len(item["color"])):
            data.append(item["color"][i])
        else:
            data.append(None)
        data.append(item["originPrice"])
        data.append(item["discountPrice"])
        data.append(item["discountRate"])
        data.append(item["screen"])
        data.append(item["operatingSystem"])
        data.append(item["frontCamera"])
        data.append(item["behindCamera"])
        data.append(item["chip"])
        data.append(item["ram"])
        data.append(item["sim"])
        data.append(item["pin"])
        data.append(item["imageUrl"][i])

        color = None
        if i < len(item["color"]):
            color = item["color"][i]
        isDuplicate = False
        for p in lstPhone:
            # Vì cùng 1 web nên check xem cùng công ty, cùng tên, cùng màu, cùng bộ nhớ, cùng hđh sẽ là 1 điện thoại
            if p.company == item["company"] and p.name == item["name"] and p.memory == item["memory"] and p.color == color and p.operatingSystem == item["operatingSystem"]:
                data.insert(0, p.id)
                oDL.Update(tuple(data))
                isDuplicate = True
                break
        
        if isDuplicate == False:
            oDL.Insert(tuple(data))

def InsertForRealDatabase():
    #oDL.DeleteRealDatabase()
    #oDL.InsertRealDBPhone()
    #oDL.InsertDBInfoPhone()
    pass

#InsertForRealDatabase()