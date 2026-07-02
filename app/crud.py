from sqlalchemy.orm import Session
from app import models, schemas

def get_pokemons(db: Session, skip: int = 0, limit: int = 100):
    return db.query(models.Pokemon).offset(skip).limit(limit).all()

def get_pokemon_by_id(db: Session, pokemon_id: int):
    return db.query(models.Pokemon).filter(models.Pokemon.id == pokemon_id).first()

def create_pokemon(db: Session, pokemon: schemas.PokemonCreate):
    db_pokemon = models.Pokemon(**pokemon.model_dump())
    db.add(db_pokemon)
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

def update_pokemon(db: Session, pokemon_id: int, pokemon_data: schemas.PokemonUpdate):
    db_pokemon = get_pokemon_by_id(db, pokemon_id)
    if not db_pokemon:
        return None
    
    update_data = pokemon_data.model_dump(exclude_unset=True)
    for key, value in update_data.items():
        setattr(db_pokemon, key, value)
        
    db.commit()
    db.refresh(db_pokemon)
    return db_pokemon

def delete_pokemon(db: Session, pokemon_id: int):
    db_pokemon = get_pokemon_by_id(db, pokemon_id)
    if db_pokemon:
        db.delete(db_pokemon)
        db.commit()
        return True
    return False
