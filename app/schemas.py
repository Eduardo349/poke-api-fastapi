from pydantic import BaseModel, ConfigDict

class PokemonBase(BaseModel):
    nome: str
    tipo: str
    pokedex_id: int

class PokemonCreate(PokemonBase):
    pass

class PokemonUpdate(BaseModel):
    nome: str | None = None
    tipo: str | None = None
    pokedex_id: int | None = None

class PokemonResponse(PokemonBase):
    id: int

    model_config = ConfigDict(from_attributes=True)

