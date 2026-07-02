### 🌟 PokéAPI Customizada - Módulo Final Backend Python

Este projeto consiste em uma API robusta desenvolvida do zero para o gerenciamento de registros de Pokémons, inspirada na PokéAPI. A aplicação foi construída utilizando práticas modernas de desenvolvimento back-end com foco em escalabilidade, conteinerização e testes automatizados.

### 🛠️ Tecnologias Utilizadas

*   **FastAPI:** Framework moderno e rápido para construção de APIs.
*   **SQLAlchemy:** ORM para mapeamento e interação com o banco de dados.
*   **PostgreSQL:** Banco de dados relacional para persistência dos dados.
*   **Docker & Docker Compose:** Isolamento e orquestração do ambiente em containers.
*   **Pytest & HTTPX:** Estrutura para testes unitários e de integração das rotas.

* * *

### 📁 Estrutura do Projeto

text

    poke-api/
    ├── app/
    │   ├── main.py          # Ponto de entrada do FastAPI e inicialização das rotas
    │   ├── config.py        # Gerenciamento de variáveis de ambiente com Pydantic Settings
    │   ├── database.py      # Configuração da sessão do SQLAlchemy e engine de conexão
    │   ├── models.py        # Modelos declarativos do banco de dados (tabelas)
    │   ├── schemas.py       # Esquemas de validação de dados com Pydantic V2
    │   └── crud.py          # Isolamento da lógica de persistência (operações de banco)
    ├── tests/
    │   └── test_main.py     # Conjunto de testes automatizados da API
    ├── Dockerfile           # Instruções de compilação da imagem da API
    ├── docker-compose.yml   # Orquestração da API e do banco com Healthcheck
    └── requirements.txt     # Dependências do ecossistema do projeto
    

Use o código com cuidado.

* * *

### 🚀 Como Executar o Projeto

Para rodar a aplicação localmente, certifique-se de ter o **Docker** instalado e que o projeto esteja fora de pastas de sincronização em nuvem (como o OneDrive).

1.  No terminal, navegue até a raiz do projeto.
2.  Execute o comando para compilar e iniciar os containers:
    
    bash
    
        docker-compose up --build
        
    
    Use o código com cuidado.
    
3.  O Docker Compose aguardará o banco de dados PostgreSQL estar totalmente pronto e saudável (*Healthy*) antes de inicializar o servidor da API.
4.  Quando o terminal indicar `Application startup complete.`, o sistema estará online.

* * *

### 📖 Documentação da API

O FastAPI gera documentações interativas de forma nativa. Com os containers em execução, você pode acessá-las pelos links abaixo:

*   **Swagger UI:** http://localhost:8000/docs (Ideal para testar os métodos `GET`, `POST`, `PUT` e `DELETE` interativamente)
*   **ReDoc:** http://localhost:8000/redoc

* * *

### 🧪 Como Executar os Testes Automatizados

Os testes validam a integridade das rotas principais da API. Para rodá-los isoladamente dentro do ambiente isolado do container, abra um novo terminal e execute:

bash

    docker-compose exec web pytest
    

Use o código com cuidado.

* * *

### 🛡️ Boas Práticas Implementadas

*   **Validação Estrita:** Uso de `ConfigDict` e tipagem explícita do Pydantic V2 para evitar inconsistências.
*   **Healthcheck do Banco:** Configuração de integridade no Docker Compose para evitar o erro de disputa de inicialização (`Connection refused`).
*   **Clean Code:** Separação clara de responsabilidades entre rotas (`main.py`), validação (`schemas.py`) e regras de persistência (`crud.py`).