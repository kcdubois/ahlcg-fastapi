from typing import Optional, List, Annotated
from pydantic import BaseModel, Field, constr


class Type(BaseModel):
    code: str = Field(min_length=1)
    name: str = Field(min_length=1)


class Faction(BaseModel):
    code: str = Field(min_length=1)
    name: str = Field(min_length=1)
    octgn_id: Optional[int] = None
    is_primary: bool


class Cycle(BaseModel):
    code: str = Field(min_length=1)
    name: str = Field(min_length=1)
    position: int = Field(ge=0)
    size: int = Field(ge=1)


class Pack(BaseModel):
    code: str = Field(min_length=1)
    cycle_code: str = Field(min_length=1)
    name: str = Field(min_length=1)
    position: int = Field(ge=1)
    date_release: Optional[str] = None
    size: Optional[int] = Field(None, ge=1)
    cgdb_id: Optional[int] = None


class Card(BaseModel):
    # Required fields
    code: Annotated[str, Field(pattern=r"^[0-9a-z]{5}[0-9a-z]?$")]
    pack_code: Annotated[str, Field(min_length=2, max_length=10)]
    position: Annotated[int, Field(ge=1)]
    quantity: Annotated[int, Field(ge=1)]

    # Fields that are required when 'name' is present
    name: Annotated[Optional[str], Field(min_length=1)]
    faction_code: Annotated[Optional[str], Field(min_length=1)]
    type_code: Annotated[Optional[str], Field(min_length=1)]

    # Optional fields
    back_text: Annotated[Optional[str], Field(min_length=1)]
    back_flavor: Annotated[Optional[str], Field()]
    cost: Optional[int]
    deck_requirements: Annotated[Optional[str], Field()]
    deck_options: Annotated[Optional[List], Field()]
    deck_limit: Annotated[Optional[int], Field(ge=0)]
    double_sided: Annotated[Optional[bool], Field()]
    duplicate_of: Optional[str] = Field(pattern=r"^[0-9a-z]{5}[0-9a-z]?$")

    # Enemy stats
    enemy_damage: Annotated[Optional[int], Field(ge=-2)]
    enemy_evade: Annotated[Optional[int], Field(ge=-2)]
    enemy_fight: Annotated[Optional[int], Field(ge=-2)]
    enemy_horror: Annotated[Optional[int], Field(ge=-2)]

    # Card properties
    exceptional: Optional[bool]
    exile: Optional[bool]
    flavor: Optional[str]
    health: Annotated[Optional[int], Field(ge=-2)]
    illustrator: Annotated[Optional[str], Field()]
    permanent: Annotated[Optional[bool], Field()]
    restrictions: Annotated[Optional[str], Field(min_length=1)]

    # Skill values
    skill_agility: Annotated[Optional[int], Field(default=0, ge=0)]
    skill_combat: Annotated[Optional[int], Field(default=0, ge=0)]
    skill_intellect: Annotated[Optional[int], Field(default=0, ge=0)]
    skill_wild: Annotated[Optional[int], Field(default=0, ge=0)]
    skill_willpower: Annotated[Optional[int], Field(default=0, ge=0)]

    # Additional attributes
    sanity: Annotated[Optional[int], Field(ge=-2)]
    slot: Annotated[Optional[str], Field(min_length=1)]
    subname: Annotated[Optional[str], Field(min_length=1)]
    subtype_code: Annotated[Optional[str], Field()]
    text: Annotated[Optional[str], Field(min_length=1)]
    traits: Annotated[Optional[str], Field()]
    victory: Annotated[Optional[int], Field(ge=0)]
    is_unique: Annotated[Optional[bool], Field()]
    xp: Annotated[Optional[int], Field(ge=0)]

    class Config:
        extra = "allow"  # Allows additional properties as specified in JSON schema

    @classmethod
    def validate_dependencies(cls, values):
        """
        Validate that if name is present, faction_code and type_code are also present
        """
        if values.get('name'):
            if not values.get('faction_code') or not values.get('type_code'):
                raise ValueError(
                    "faction_code and type_code are required when name is present")
        return values
