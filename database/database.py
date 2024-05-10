from pymongo.mongo_client import MongoClient
from certifi import where

uri = "mongodb+srv://codificador10:jackyChan@cluster0.5dhnzzl.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0"
client = MongoClient(uri, tlsCAFile=where())

db=client.functionsInfo
collection_name= db["functions_Info"]
