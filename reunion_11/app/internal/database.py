# Database me crea una conexion con la base de datos mongodb
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database
from typing import Optional
import os
from dotenv import load_dotenv


# Cargar variables de entorno desde un archivo .env
load_dotenv()

# Configuracion de la base de datos desde variables de entorno
MONGO_USER = os.getenv("MONGO_USER", "root")
MONGO_PASSWORD = os.getenv("MONGO_PASSWORD", "example")
MONGO_HOST = os.getenv("MONGO_HOST", "localhost")
MONGO_PORT = os.getenv("MONGO_PORT", "27017")
MONGO_DB = os.getenv("MONGO_DB", "e-commerce")
MONGO_URI = f"mongodb://{MONGO_USER}:{MONGO_PASSWORD}@{MONGO_HOST}:{MONGO_PORT}/"


class DatabaseConnection:
    def __init__(self):
        self.client: Optional[MongoClient] = None
        self.db: Optional[Database] = None

    def connect(self):
        self.client = MongoClient(MONGO_URI)
        self.db = self.client[MONGO_DB]

    def get_collection(self, name: str) -> Collection:
        if self.db is None:
            raise Exception("Database not connected")
        return self.db[name]

    def close(self):
        if self.client:
            self.client.close()
