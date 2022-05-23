import mysql.connector
from mysql.connector import errorcode
from item import TgddPhoneItem

config = {
  'user': 'root',
  'password': '1234',
  'host': '127.0.0.1',
  'database': 'tgdd_phone',
  'port' : '3308',
  'raise_on_warnings': True
}

conn = mysql.connector.connect(**config)

class DL():

    def GetAll(self):
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM mobiphone")
        records = cursor.fetchall()

        result = []
        for row in records:
            phone = TgddPhoneItem()
            phone.id = row["RefID"]
            phone.company = row["Company"]
            phone.name = row["Name"]
            phone.memory = row["Memory"]
            phone.color = row["Color"]
            phone.originPrice = row["OriginPrice"]
            phone.discountPrice = row["DiscountPrice"]
            phone.discountRate = row["DiscountRate"]
            phone.screen = row["Screen"]
            phone.operatingSystem = row["OperatingSystem"]
            phone.frontCamera = row["FrontCamera"]
            phone.behindCamera = row["BehindCamera"]
            phone.chip = row["Chip"]
            phone.ram = row["Ram"]
            phone.sim = row["Sim"]
            phone.pin = row["Pin"]
            phone.imageUrl = row["ImageUrl"]

            result.append(phone)
            
        return result