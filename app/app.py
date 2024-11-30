import fastapi

from models import Card

app = fastapi.FastAPI()


@app.get("/")
async def root():
    return {"status": "ok"}


@app.get("/cards")
async def get_cards() -> list[Card]:
    return {"cards": []}


@app.get("/cards/{code}")
async def get_card(code: str) -> Card:
    return {"card": {"code": code, "name": "Card Name"}}


@app.post("/cards")
async def create_card(card: Card) -> Card:
    return card
