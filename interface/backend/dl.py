from unittest import result
from elasticsearch import Elasticsearch
import mysql.connector
from mysql.connector import Error
from pymysql import NULL
import json

config = {
  'user': 'root',
  'password': '1234',
  'host': '127.0.0.1',
  'database': 'integration_phone',
  'port' : '3308',
  'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)

es = Elasticsearch("http://localhost:9200")

class DL:
    def __init__(self) -> None:
        pass
    
    # Lấy ds điện thoại phù hợp trên elasticsearch
    def getPhoneMatching(self, name):
        request_body = {
                "query": {
                    "bool" : { 
                        "should": [
                            { "match": { "PhoneName": name }}
                            ] 
                        }
                    },
                    "track_total_hits": True,
                    "size": 100
                }

        res = es.search(index="integration_phone", body=request_body)
        return res["hits"]["hits"]

    # Lấy ds điện thoại từ mysql 
    def getPhone(self, listData):
        lstRefID = []
        for item in listData:
            lstRefID.append(item.get("RefID"))

        format_strings = ','.join(['%s'] * len(lstRefID))
        sql = "Select * From phone p Where p.RefID IN (%s)" % format_strings
        sqlRefencer = "Select * From referencephone r Where r.ReferenceID IN (%s)" % format_strings

        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql, tuple(lstRefID))
        records = cursor.fetchall()

        cursor.execute(sqlRefencer, tuple(lstRefID))
        recordsRef = cursor.fetchall()

        result = []
        for item in records:
            result.append(item)
            for phone in recordsRef:
                if phone.get("ReferenceID") == item.get("RefID"):
                    result.append(phone)

        return result

    def getAll(self, rom, ram):
        sql = ""
        sqlRefencer = ""
        if rom != "" and ram == "":
            sql = "Select * From phone p Where p.Memory = %s " % (int(rom))
            sqlRefencer = "Select * From referencephone p Where p.Memory = %s " % (int(rom))
        elif rom == "" and ram != "":
            sql = "Select * From phone p Where p.Ram = %s " % (int(ram))
            sqlRefencer = "Select * From referencephone p Where p.Ram = %s " % (int(ram))
        elif rom != "" and ram != "":
            sql = "Select * From phone p Where p.Memory = %s AND p.Ram = %s " % (int(rom), int(ram))
            sqlRefencer = "Select * From referencephone p Where p.Memory = %s AND p.Ram = %s " % (int(rom), int(ram))
        else:
            sql = "Select * From phone"
            sqlRefencer = "Select * From referencephone"

        cursor = conn.cursor(dictionary=True)
        cursor.execute(sql)
        records = cursor.fetchall()

        cursor.execute(sqlRefencer)
        recordsRef = cursor.fetchall()

        result = []
        for item in records:
            result.append(item)
            for phone in recordsRef:
                if phone.get("ReferenceID") == item.get("RefID"):
                    result.append(phone)

        return result