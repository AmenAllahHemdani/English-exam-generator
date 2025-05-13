import pymongo
from dotenv import dotenv_values

config = dotenv_values(".env")

myclient = pymongo.MongoClient(config["ATLAS_URI"])

mydb = myclient[config["DB_NAME"]]
mycol = mydb[config["DB_NAME"]]

def insert(data):
  x = mycol.insert_one(data)

def loading(value):
  result = []
  myquery = {"chapter": value}
  data = mycol.find(myquery,{"_id": 0, "chapter": 1, "date": 1 ,"content" : 1}).sort("date",-1)
  for item in data:
    result.append(item)
  return result