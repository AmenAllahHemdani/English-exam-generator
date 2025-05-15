import pymongo
from dotenv import dotenv_values

config = dotenv_values(".env")

client = pymongo.MongoClient(config["ATLAS_URI"])

db = client[config["DB_NAME"]]

table = db[config["DB_NAME"]]

def insert(data):
  x = table.insert_one(data)

def loading(value):
  result = []
  myquery = {"chapter": value}
  data = table.find(myquery,{"_id": 0, "chapter": 1, "date": 1 ,"content" : 1}).sort("date",-1)
  for item in data:
    result.append(item)
  return result