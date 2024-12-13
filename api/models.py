from typing import Optional, List, Annotated
from pydantic import BaseModel, ConfigDict


class Card(BaseModel):
    # Required fields
    code: str
    pack_code: str
    position: int
    quantity: int

    # Fields that are required when 'name' is present
    name: str
    faction_code: str | None = None
    type_code: str | None = None

    # Optional fields
    back_text: str | None = None
    back_flavor: str | None = None
    cost: int | None = None
    deck_requirements: str | None = None
    deck_options: list | None = None
    deck_limit: int | None = None
    double_sided: bool | None = None
    duplicate_of: str | None = None

    # Enemy stats
    enemy_damage: int | None = None
    enemy_evade: int | None = None
    enemy_fight: int | None = None
    enemy_horror: int | None = None

    # Card properties
    exceptional: bool = False
    exile: bool = False
    flavor: str | None = None
    health: int | None = None
    illustrator: str | None = None
    permanent: bool = False
    restrictions: str | None = None

    # Skill values
    skill_agility: int | None = None
    skill_combat: int | None = None
    skill_intellect: int | None = None
    skill_wild: int | None = None
    skill_willpower: int | None = None

    # Additional attributes
    sanity: int | None = None
    slot: str | None = None
    subname: str | None = None
    subtype_code: str | None = None
    text: str | None = None
    traits: str | None = None
    victory: int | None = None
    is_unique: bool | None = None
    xp: int | None = None

    model_config = ConfigDict(extra="allow")
