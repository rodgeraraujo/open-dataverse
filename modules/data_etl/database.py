import os
import pymongo

def connection():
    client = pymongo.MongoClient(os.environ.get('DB'))
    return client