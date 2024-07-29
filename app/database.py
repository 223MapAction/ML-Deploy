# app/database.py
from databases import Database

DATABASE_URL = "postgresql://root:postges@139.144.63.238/mapaction"
database = Database(DATABASE_URL)


async def connect():
    await database.connect()


async def disconnect():
    await database.disconnect()


async def fetch_one(query):
    return await database.fetch_one(query)
