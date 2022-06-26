from unittest import result
from fuzzywuzzy import process
import json
import distance
import threading
import mysql.connector
from mysql.connector import Error
from pymysql import NULL
import uuid
from elasticsearch import Elasticsearch

from matplotlib.pyplot import phase_spectrum

config = {
  'user': 'root',
  'password': '1234',
  'host': '127.0.0.1',
  'database': 'integration_phone',
  'port' : '3308',
  'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)

class MatchingData:

    dataCellPhone = []
    dataFPhone = []
    dataPhongVu = []
    dataTGDD = []

    dataMatching = []
    finalMatching = []

    def __init__(self) -> None:
        pass
    
    # Đơn giản là chuyển từ file json thành list
    def LoadData(self):
        f_listCellPhone = open("data_cellphone.json", "r", encoding="utf-8-sig")
        self.dataCellPhone = json.load(f_listCellPhone)
        f_listFPhone = open("data_fphone.json", "r", encoding="utf-8-sig")
        self.dataFPhone = json.load(f_listFPhone)
        f_listPhongVu = open("data_pvphone.json", "r", encoding="utf-8-sig")
        self.dataPhongVu = json.load(f_listPhongVu)
        f_listTGDD = open("data_tgddphone.json", "r", encoding="utf-8-sig")
        self.dataTGDD = json.load(f_listTGDD)

        f_listCellPhone.close()
        f_listFPhone.close()
        f_listPhongVu.close()
        f_listTGDD.close()

    # Matching 2 tập dữ liệu với nhau
    def MatchingData(self, tagert, source, typeFunc):
        result = []
        dataNotMatching = []
        for i in range(len(tagert)):
            dic = {}
            lstData = []
            # Kiểm tra xem đối tượng đích là một dict hay là 1 list các object
            # Nếu là 1 list thì lấy ra object đầu tiên làm đại diện
            # tính toán độ tương đồng trên object đó
            # Nếu là 1 dict thì đơn giản là lấy nó ra mà so sánh thui :>
            if type(tagert[i]) != list:
                lstData.append(tagert[i])
            else:
                lstData = tagert[i]
            dic[i] = lstData
            result.append(dic)

        for k in range(len(source)):
            items = source[k]
            item = {}

            isList = False
            lstItem = []
            if len(items.keys()) == 1:
                isList = True
                lstItem = items.get(k)
            # Đối với đối tượng nguồn cũng làm tương tự với đối tượng đích ở trên
            if isList == True:
                item = items.get(k)[0]
            else:
                item = items

            listMatch = []

            for i in range(len(tagert)):
                phone = {}

                if len(tagert[i].keys()) == 1:
                    phone = tagert[i].get(i)[0]
                else:
                    phone = tagert[i]
                # Rule: nếu cùng bộ nhớ, cùng ram, cùng màu thì mới so sánh tiếp
                # Nếu bị null thì coi như là không cùng loại luôn, đỡ phải xét
                if item["Memory"] == phone["Memory"] and item["Ram"] == phone["Ram"] and item["Color"] == phone["Color"]:
                    dicP = {}
                    dicP[i] = phone
                    listMatch.append(dicP)

            if len(listMatch) == 0:
                # Nếu không có candidate nào ok thì
                # Kiểm tra xem items là list hay dict
                # Nếu là list thì thêm cả list đó vào danh sách không thể ghép nối, còn dict thì thêm nó vào thôi
                if isList == True:
                    lstNotMatch = []
                    for phoneNotMatch in lstItem:
                        lstNotMatch.append(phoneNotMatch)
                    dataNotMatching.append(lstNotMatch)
                else:
                    dataNotMatching.append(item)
            else:
                dataTest = []
                for i in range(len(listMatch)):
                    phoneName = listMatch[i].get(list(listMatch[i].keys())[0])["PhoneName"]
                    dataTest.append(phoneName.lower())
                # Dùng fuzzy để chọn ra candidate có điểm số cao nhất
                fitName = process.extractOne(item["PhoneName"].lower(), dataTest)[0]
                for match in listMatch:
                    if match.get(list(match.keys())[0])["PhoneName"].lower() == fitName:
                        # Dùng thêm Jascard để check nữa cho chuẩn bài
                        disTance = 1 - distance.jaccard(item["PhoneName"].lower(), fitName)
                        if disTance > 0.7:
                            index = list(match.keys())[0]
                            listPhone = result[index].get(index)

                            # Đoạn này và mấy đoạn tương tự ở dưới là 
                            # để lấy cả list danh sách để append vào
                            if isList == True:
                                for phoneMatch in lstItem:
                                    listPhone.append(phoneMatch)
                            else:
                                listPhone.append(item)

                            result[index][index] = listPhone
                        else:
                            if isList == True:
                                lstNotMatch = []
                                for phoneNotMatch in lstItem:
                                    lstNotMatch.append(phoneNotMatch)
                                dataNotMatching.append(lstNotMatch)
                            else:
                                dataNotMatching.append(item)    

        # Nếu không thêm được vào cụm nào thì tạo 1 cụm mới và thêm nó vào
        if len(dataNotMatching) > 0:
            lastIndex = len(result)
            for item in dataNotMatching:
                dicP2 = {}
                if type(item) != list:
                    lst = []
                    lst.append(item)
                    dicP2[lastIndex] = lst
                else:
                    dicP2[lastIndex] = item
                result.append(dicP2)
                lastIndex = lastIndex + 1

        # Nếu 1 thì là bước ghép cuối cùng
        if typeFunc == 0:
            self.dataMatching.append(result)
        else:
            self.finalMatching = result


    # Tạo thread để ghép x2 tốc độ nè
    # Ghép dữ liệu từ 4 file thành 1
    def Matching(self):
        thread1 = threading.Thread(target=self.MatchingData, args=(self.dataCellPhone, self.dataFPhone, 0))
        thread2 = threading.Thread(target=self.MatchingData, args=(self.dataPhongVu, self.dataTGDD, 0))

        thread1.start()
        thread2.start()

        thread1.join()
        thread2.join()

        # Đợi 2 thread chạy xong mới chạy nốt matching cuối cùng
        self.MatchingData(self.dataMatching[0], self.dataMatching[1], 1)
        self.CleanData()

        
    # Làm sạch data trước khi save
    def CleanData(self):
        result = []
        for i in range(len(self.finalMatching)):
            dic = {}
            item = self.finalMatching[i]
            tmp = []
            phoneList = item.get(i)

            for j in range(0, len(phoneList)):
                item = phoneList[j]
                if len(item.keys()) == 1:
                    phone = item.get(i)
                    for p in phone:
                        tmp.append(p)
                else:
                    tmp.append(item)

            dic[i] = tmp
            result.append(dic)
        
        self.finalMatching = result

    # Lưu dữ liệu xuống mysql
    def SaveDataToMySQL(self):
        data = self.finalMatching

        sql = "INSERT INTO phone(RefID, PhoneName, Price, Image, Color, Memory, Ram, Chip, FrontCamera, BehindCamera, OperationSystem, Screen, IdPhone, Producer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        sqlReference = "INSERT INTO referencephone(RefID, ReferenceID, PhoneName, Price, Image, Color, Memory, Ram, Chip, FrontCamera, BehindCamera, OperationSystem, Screen, IdPhone, Producer) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
        recordInsert = []
        recordInsertReference = []
        for i in range(len(data)):
            items = data[i].get(i)
            if len(items) == 0:
                recordInsert.append((str(uuid.uuid4()), items.get("PhoneName"), items.get("Price"), items.get("Image"), items.get("Color"), items.get("Memory"), items.get("Ram"), items.get("Chip"), items.get("FrontCamera"), items.get("BehindCamera"), items.get("OperationSystem"), items.get("Screen"), items.get("IdPhone"), items.get("Producer")))
            else:
                item = items[0]
                refID = str(uuid.uuid4())
                recordInsert.append((refID, item.get("PhoneName"), item.get("Price"), item.get("Image"), item.get("Color"), item.get("Memory"), item.get("Ram"), item.get("Chip"), item.get("FrontCamera"), item.get("BehindCamera"), item.get("OperationSystem"), item.get("Screen"), item.get("IdPhone"), item.get("Producer")))
                
                for j in range(1, len(items)):
                    phone = items[j]
                    recordInsertReference.append((str(uuid.uuid4()), refID, phone.get("PhoneName"), phone.get("Price"), phone.get("Image"), phone.get("Color"), phone.get("Memory"), phone.get("Ram"), phone.get("Chip"), phone.get("FrontCamera"), phone.get("BehindCamera"), phone.get("OperationSystem"), phone.get("Screen"), phone.get("IdPhone"), phone.get("Producer")))


        cursor = conn.cursor(dictionary=True)
        cursor.executemany(sql, recordInsert)
        conn.commit()

        cursor.executemany(sqlReference, recordInsertReference)
        conn.commit()
        cursor.close()
    
    # Lưu dữ liệu xuống elasticsearch
    def SaveDataToElasticsearch(self):
        es = Elasticsearch("http://localhost:9200")
        # es = Elasticsearch()
        # Tạo index để lưu data
        if es.indices.exists(index="integration_phone") == True:
            es.indices.delete(index="integration_phone")
        es.indices.create(index="integration_phone")
        # Lấy dữ liệu từ mysql để lưu lên elasticsearch
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT p.RefID, p.PhoneName FROM phone p")
        records = cursor.fetchall()
        cursor.close()

        # Do số lượng bản ghi nhiều => Nếu gọi từng request 1 để push data lên sẽ rất lâu
        # Nên tạo ra file import đuôi là txt; xong đổi đuôi về json, (vì nếu để là json thì nó ném lỗi vào mặt ngay) 
        # Rồi chạy bằng lệnh trên console
        # curl -s -H "Content-Type: application/x-ndjson" -XPOST localhost:9200/_bulk --data-binary "@data_to_elasticsearch.json"
        data = open('data_to_elasticsearch.txt', 'w', encoding='utf-8-sig')
        id = 0
        for i in range(len(records)):
            tmp = "{\"index\": {\"_index\": \"integration_phone\", \"_id\": "+ str(id)+"}}"
            data.write(tmp)
            data.write("\n")
            tmp = json.dumps(records[i], ensure_ascii=False)
            data.write(tmp)
            data.write("\n")
            id = id+1
        
    
if __name__ == "__main__":
    matchingData = MatchingData()
    # matchingData.LoadData()
    # matchingData.Matching()
    # matchingData.SaveDataToMySQL()
    # matchingData.SaveDataToElasticsearch()

    