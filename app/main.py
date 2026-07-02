from fastapi import FastAPI, Depends, HTTPException, status
from sqlalchemy.orm import Session
from typing import List

from app import crud, models, schemas, database

# Cria as tabelas ao iniciar a aplicação (para fins de simplificação)
database.Base.metadata.create_all(bind=database.engine)

app = FastAPI(
    title="PokéAPI Customizada",
    description="API para gerenciamento de Pokémons - Módulo Final Backend Python",
    version="1.0.0"
)

@app.post("/pokemons", response_model=schemas.PokemonResponse, status_code=status.HTTP_201_CREATED)
def criar_pokemon(pokemon: schemas.PokemonCreate, db: Session = Depends(database.get_db)):
    return crud.create_pokemon(db=db, pokemon=pokemon)

@app.get("/pokemons", response_model=List[schemas.PokemonResponse])
def listar_pokemons(skip: int = 0, limit: int = 100, db: Session = Depends(database.get_db)):
    return crud.get_pokemons(db, skip=skip, limit=limit)

@app.get("/pokemons/{pokemon_id}", response_model=schemas.PokemonResponse)
def buscar_pokemon(pokemon_id: int, db: Session = Depends(database.get_db)):
    db_pokemon = crud.get_pokemon_by_id(db, pokemon_id=pokemon_id)
    if db_pokemon is None:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")
    return db_pokemon

@app.put("/pokemons/{pokemon_id}", response_model=schemas.PokemonResponse)
def atualizar_pokemon(pokemon_id: int, pokemon: schemas.PokemonUpdate, db: Session = Depends(database.get_db)):
    db_pokemon = crud.update_pokemon(db, pokemon_id=pokemon_id, pokemon_data=pokemon)
    if db_pokemon is None:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")
    return db_pokemon

@app.delete("/pokemons/{pokemon_id}", status_code=status.HTTP_204_NO_CONTENT)
def deletar_pokemon(pokemon_id: int, db: Session = Depends(database.get_db)):
    sucesso = crud.delete_pokemon(db, pokemon_id=pokemon_id)
    if not sucesso:
        raise HTTPException(status_code=404, detail="Pokémon não encontrado")
