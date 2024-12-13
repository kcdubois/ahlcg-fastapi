import fastapi

from models import Card
import client

app = fastapi.FastAPI()

@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/cards")
async def get_cards() -> list[Card]:
    result = await client.get_cards()
    return result


@app.get("/cards/{code}")
async def get_card(code: str) -> Card:
    result = await client.get_card(code)
    return result

@app.post("/cards")
async def create_card(card: Card) -> Card:
    result = await client.create_card(card)
    return result

@app.put("/cards/{code}")
async def update_card(code: str, card: Card) -> Card:
    return await client.update_card(code, card)


@app.delete("/cards/{code}")
async def delete_card(code: str) -> None:
    return await client.delete_card(code)
