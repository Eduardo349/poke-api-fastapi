from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_criar_pokemon():
    # Usando o Charmander (ID 4) para não dar conflito com o Pikachu (ID 25)
    response = client.post(
        "/pokemons",
        json={"nome": "Charmander", "tipo": "Fogo", "pokedex_id": 4},
    )
    assert response.status_code == 201
    data = response.json()
    assert data["nome"] == "Charmander"
    assert "id" in data

def test_listar_pokemons():
    response = client.get("/pokemons")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

