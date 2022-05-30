import mysql.connector
from mysql.connector import Error
from pymysql import NULL
from item import TgddPhoneItem
import uuid

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
      
      cursor.close()
      return result
  
  def Insert(self, item):
    try:
      cursor = conn.cursor()
      cursor.callproc('Proc_Insert_Phone', item)
      conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()

  def Update(self, item):
    try:
      cursor = conn.cursor()
      cursor.callproc('Proc_Update_Phone', item)
      conn.commit()
    except Error as e:
        print(e)
    finally:
        cursor.close()

  def GetRealAll(self):
      cursor = conn.cursor(dictionary=True)
      cursor.execute("SELECT p.RefID FROM phone p")
      records = cursor.fetchall()

      result = []
      for row in records:
          phone = TgddPhoneItem()
          phone.id = row["RefID"]

          result.append(phone)
      
      cursor.close()
      return result

  def DeleteRealDatabase(self):
    cursor = conn.cursor(dictionary=True)
    cursor.execute("DELETE FROM phone")
    conn.commit()

    cursor.execute("DELETE FROM phoneinformation")
    conn.commit()

    cursor.execute("DELETE FROM phoneimage")
    conn.commit()
    cursor.close()

  def InsertRealDBPhone(self):
    phone = self.GetAll()

    sqlPhone = "INSERT INTO phone(RefID,Name,Company,OriginPrice,DiscountPrice,DiscountRate,Color) VALUES (%s, %s, %s, %s, %s, %s, %s)"
    recordsToInsert = []
    for p in phone:
      recordsToInsert.append((str(uuid.uuid4()), p.name, p.company, p.originPrice, p.discountPrice, p.discountRate, p.color))
      
    cursor = conn.cursor(dictionary=True)
    cursor.executemany(sqlPhone, recordsToInsert)
    conn.commit()
    cursor.close()

  def InsertDBInfoPhone(self):
    phone = self.GetAll()

    lstPhone = self.GetRealAll()

    sqlPhoneInfo = "INSERT INTO phoneinformation(RefID,PhoneID,Memory,Chip,Ram,Sim,Pin,FrontCamera,BehindCamera,Screen,OperatingSystem) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
    sqlPhoneImage = "INSERT INTO phoneimage(RefID,PhoneID,ImageUrl) VALUES (%s, %s, %s)"
    recordInsertInfo = []
    recordInsertImage = []
    i = 0
    for p in lstPhone:
      recordInsertInfo.append((str(uuid.uuid4()), p.id, phone[i].memory, phone[i].chip, phone[i].ram, phone[i].sim, phone[i].pin, phone[i].frontCamera, phone[i].behindCamera, phone[i].screen, phone[i].operatingSystem))
      recordInsertImage.append((str(uuid.uuid4()), p.id, phone[i].imageUrl))
      i = i+1

    cursor = conn.cursor(dictionary=True)
    cursor.executemany(sqlPhoneInfo, recordInsertInfo)
    conn.commit()

    cursor.executemany(sqlPhoneImage, recordInsertImage)
    conn.commit()
    cursor.close()


