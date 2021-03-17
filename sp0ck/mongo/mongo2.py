import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["testdb"]

collection = db["numbers"]

for x in collection.find():
    print(x)
