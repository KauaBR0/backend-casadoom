from motor.motor_asyncio import AsyncIOMotorClient
from typing import Optional

class MongoDB:
    client: Optional[AsyncIOMotorClient] = None
    database_name = "casadoom_db"

    @classmethod
    async def connect_db(cls):
        cls.client = AsyncIOMotorClient("mongodb://localhost:27017")
        cls.db = cls.client[cls.database_name]

    @classmethod
    async def close_db(cls):
        if cls.client:
            cls.client.close()

    @classmethod
    def get_db(cls):
        return cls.db

    @classmethod
    def get_collection(cls, collection_name: str):
        return cls.db[collection_name]
