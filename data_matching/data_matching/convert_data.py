import json

class DataMatching:

    mediateCellPhone = {}
    mediateFPhone = {}
    mediatePhongVu = {}
    mediateTGDD = {}

    dataCellPhone = []
    dataFPhone = []
    dataPhongVu = []
    dataTGDD = []

    def __init__(self) -> None:
        pass
    
    # Tạo liên kết giữa mediate với từng view
    # từ file schema đã có
    def CreateSchemaMatching(self):
        fileMediateCellPhone = open('schema_matching/mediate-han.nn.txt', 'r')
        self.mediateCellPhone = self.BuildDictionSchemaMatching(fileMediateCellPhone)        
        
        fileMediateFPhone = open('schema_matching/mediate-hai.nh.txt', 'r')
        self.mediateFPhone = self.BuildDictionSchemaMatching(fileMediateFPhone)

        fileMediatePhongVu = open('schema_matching/mediate-hang.vtt.txt', 'r')
        self.mediatePhongVu = self.BuildDictionSchemaMatching(fileMediatePhongVu)

        fileMediateTGDD = open('schema_matching/mediate-ha.tq.txt', 'r')
        self.mediateTGDD = self.BuildDictionSchemaMatching(fileMediateTGDD)

        fileMediateCellPhone.close()
        fileMediateFPhone.close()
        fileMediatePhongVu.close()
        fileMediateTGDD.close()
        pass
    
    # Đọc file schema
    def BuildDictionSchemaMatching(self, file):
        lines = file.readlines()
        dic = {}
        for line in lines:
            matching = line.strip()
            mediate = matching.split(",")[0].split("__")[1][0: -1]
            view = matching.split(",")[1]
            if view != " '')":
                view = view.split("__")[1][0: -2]
            else:
                view = None
            dic[mediate] = view
        
        return dic

    # Convert lại data từ view thành
    # mediate cho chuẩn
    def ConvertData(self):
        f_listCellPhone = open("../finaldata/cellphone.json", "r", encoding="utf-8-sig")
        listCellPhone = json.load(f_listCellPhone)
        f_listFPhone = open("../finaldata/fpt.json", "r", encoding="utf-8-sig")
        listFPhone = json.load(f_listFPhone)
        f_listPhongVu = open("../finaldata/phongvu.json", "r", encoding="utf-8-sig")
        listPhongVu = json.load(f_listPhongVu)
        f_listTGDD = open("../finaldata/tgdd.json", "r", encoding="utf-8-sig")
        listTGDD = json.load(f_listTGDD)
        
        self.dataCellPhone = self.ExcuteConvertData(listCellPhone, self.mediateCellPhone, "CellPhone")
        self.dataFPhone = self.ExcuteConvertData(listFPhone, self.mediateFPhone, "FPhone")
        self.dataPhongVu = self.ExcuteConvertData(listPhongVu, self.mediatePhongVu, "PhongVu")
        self.dataTGDD = self.ExcuteConvertData(listTGDD, self.mediateTGDD, "TGDD")

        with open('data_cellphone.json', 'w', encoding='utf-8') as f:
            json.dump(self.dataCellPhone, f, ensure_ascii=False, indent=4)

        with open('data_fphone.json', 'w', encoding='utf-8') as f:
            json.dump(self.dataFPhone, f, ensure_ascii=False, indent=4)

        with open('data_pvphone.json', 'w', encoding='utf-8') as f:
            json.dump(self.dataPhongVu, f, ensure_ascii=False, indent=4)

        with open('data_tgddphone.json', 'w', encoding='utf-8') as f:
            json.dump(self.dataTGDD, f, ensure_ascii=False, indent=4)

        f_listCellPhone.close()
        f_listFPhone.close()
        f_listPhongVu.close()
        f_listTGDD.close()
        pass
    
    # Thực hiện convert
    def ExcuteConvertData(self, data, dictionary, idData):
        result = []
        for item in data:
            dic = {}
            for key in dictionary:
                if key == "PhoneID":
                    continue
                if dictionary.get(key) == None:
                    dic[key] = None
                else:
                    dic[key] = item[dictionary.get(key)]
            dic["IdPhone"] = idData
            result.append(dic)

        return result


if __name__ == "__main__":
    dataMatching = DataMatching()
    dataMatching.CreateSchemaMatching()
    dataMatching.ConvertData()