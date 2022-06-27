import mysql.connector
from mysql.connector import Error
from pymysql import NULL
import json

config = {
  'user': 'root',
  'password': '1234',
  'host': '127.0.0.1',
  'database': 'tgdd_phone',
  'port' : '3308',
  'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)

cursor = conn.cursor(dictionary=True)
cursor.execute("SELECT * FROM mobiphone")
records = cursor.fetchall()

result = []
for row in records:
    phone = {}
    phone["Company"] = row["Company"]
    phone["Name"] = row["Name"]
    phone["Memory"] = row["Memory"]
    phone["Color"] = row["Color"]
    phone["OriginPrice"] = row["OriginPrice"]
    phone["DiscountPrice"] = row["DiscountPrice"]
    phone["DiscountRate"] = row["DiscountRate"]
    phone["Screen"] = row["Screen"]
    phone["OperatingSystem"] = row["OperatingSystem"]
    phone["FrontCamera"] = row["FrontCamera"]
    phone["BehindCamera"] = row["BehindCamera"]
    phone["Chip"] = row["Chip"]
    phone["Ram"] = row["Ram"]
    phone["Sim"] = row["Sim"]
    phone["Pin"] = row["Pin"]
    phone["ImageUrl"] = row["ImageUrl"]

    result.append(phone)

cursor.close()

with open('data_tgdd.json', 'w', encoding='utf-8') as f:
    json.dump(result, f, ensure_ascii=False, indent=4)