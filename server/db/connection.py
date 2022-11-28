from pymongo import MongoClient

client = MongoClient("mongodb://rlruser:rlrpassword@rlr-mongo:27017/")

db = client.rlrdb
