from pymongo import MongoClient, AsyncMongoClient

from config import settings
from models import Card

client = AsyncMongoClient(
    host=settings.mongo_host,
    port=settings.mongo_port,
    username=settings.mongo_username,
    password=settings.mongo_password,
)

db = client[settings.mongo_db]


class CardClient:
    """Client for the cards collection."""

    def __init__(self, client: AsyncMongoClient):
        self._collection = client[settings.mongo_collection]

    async def get_cards(self) -> list[Card]:
        return await self._collection.find().to_list()

    async def create_card(self, card: Card) -> Card:
        return await self._collection.insert_one(card.model_dump())

    async def create_bulk_cards(self, cards: list[Card]) -> list[Card]:
        return await self._collection.insert_many(cards)

    async def update_card(self, code: str, card: Card) -> Card:
        return await self._collection.update_one({"code": code}, {"$set": card.model_dump()})

    async def delete_card(self, code: str) -> None:
        return await self._collection.delete_one({"code": code})
