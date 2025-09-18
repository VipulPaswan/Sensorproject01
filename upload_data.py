from pymongo.mongo_client import MongoClient
import pandas as pd
import json

#url
uri = "mongodb+srv://vipul:12345@cluster0.3uhnlh7.mongodb.net/?retryWrites=true&w=majority"

#create a new client and connect to server
client = MongoClient(uri)


#create a database name and collection name
DATABASE_NAME = "pwskills"
COLLECTION_NAME = "testfault"

df = pd.read_csv("C:\Users\LENOVO\OneDrive\Desktop\Sensor Project\notebook\data\wafer_23012020_041211.csv")
df.head()

df=df.drop("Unnamed: 0",axis=1)

json_record = list(json.loads(df.T.to_json()).values())

