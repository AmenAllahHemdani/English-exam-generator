import pymongo
from dotenv import dotenv_values

config = dotenv_values(".env")

client = pymongo.MongoClient(config["ATLAS_URI"])

db = client[config["DB_NAME"]]

table = db[config["DB_NAME"]]
