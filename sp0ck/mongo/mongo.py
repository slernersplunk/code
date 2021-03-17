import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

db = client["testdb"]

collection = db["numbers"]

dictionary = { "number": "1" }

x = collection.insert_one(dictionary)

print (x.inserted_id)
