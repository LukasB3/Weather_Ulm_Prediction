from pymongo import MongoClient

from getData_1h import weather_dict

client = MongoClient('mongodb+srv://Test:WeatherUlm@weathercluster.zhdkvmz.mongodb.net/?retryWrites=true&w=majority')

db = client['Weather_Ulm']
collection = db['data_1h']

collection.insert_one(weather_dict)

client.close()