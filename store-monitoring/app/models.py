from pymongo import MongoClient
import os

class MongoDB:
    def __init__(self):
        self.client = MongoClient(os.getenv('MONGO_URI', 'mongodb://localhost:27017/store_monitoring'))
        self.db = self.client.store_monitoring

# Create a single instance of MongoDB
mongo_db_instance = MongoDB()

def get_store_status_collection():
    return mongo_db_instance.db.store_status

def get_business_hours_collection():
    return mongo_db_instance.db.business_hours

def get_store_timezone_collection():
    return mongo_db_instance.db.store_timezone
