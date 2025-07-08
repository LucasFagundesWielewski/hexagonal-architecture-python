import os

from pymongo import MongoClient
from pymongo.database import Database

def get_db() -> Database:
    connection_str = os.environ.get("MONGO_CONNECTION_STRING", "mongodb://localhost:27017")
    db_name = os.environ.get("MONGO_DB_NAME", "hexagonal_architecture_python")

    mongo_client: MongoClient = MongoClient(connection_str, serverSelectionTimeoutMS=5)
    database =  mongo_client.get_database(db_name)

    return database