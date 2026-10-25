# 🚀 API RESTful de Gerenciamento de Tarefas com FastAPI e IA

API de gerenciamento de tarefas (To-Do List) desenvolvida em **Python** e **FastAPI** como parte do projeto prático de pós-graduação. O sistema conta com uma arquitetura em camadas limpa, persistência relacional transacional e um serviço inteligente de priorização de tarefas assistido por Inteligência Artificial.

---

## 🛠️ Tecnologias e Stack
* **Linguagem:** Python 3.12+
* **Framework Web:** FastAPI (Assíncrono e de alta performance)
* **Persistência / ORM:** SQLAlchemy com SQLite (Banco local em arquivo e isolamento em memória para testes)
* **Validação de Dados:** Pydantic V2 (DTOs e tipagem estrita)
* **Testes Automatizados:** Pytest (Suíte de integração isolada)
* **Servidor ASGI:** Uvicorn

---

## 📋 Funcionalidades Implementadas
- **CRUD Completo:** Criação, listagem geral, consulta por ID, atualização parcial (`PATCH`) e exclusão de tarefas.
- **Gestão de Estados:** Controlo de tarefas por status (`pending` / `completed`).
- **Filtros Dinâmicos:** Filtragem avançada através de *Query Parameters*.
- **Persistência Real:** Os dados são gravados num ficheiro local (`tasks.db`), garantindo que não se perdem ao reiniciar a aplicação.
- **Priorização Inteligente por IA:** Módulo de serviços dedicado (`AITaskService`) com normalização de acentos para detetar e sugerir automaticamente a prioridade das tarefas.
- **Validação e Tratamento de Erros:** Respostas HTTP padronizadas (`201 Created`, `200 OK`, `404 Not Found`, `422 Unprocessable Entity`).
- **Health Check:** Endpoint dedicado em `/health` para monitorização de saúde da aplicação.
- **Documentação Automática:** Swagger UI interativo integrado em `/docs`.

---

## 🏛️ Arquitetura do Projeto
O projeto segue o padrão de **Arquitetura em Camadas (Separation of Concerns)**, garantindo baixo acoplamento e alta testabilidade:

```text
Cliente HTTP
  -> FastAPI Router (app/routers/)          # Camada de Apresentação / Endpoints
  -> Schemas Pydantic (app/schemas/)        # Validação de Dados e DTOs
  -> TaskService (app/services/)            # Regras de Negócio e IA
  -> TaskRepository (app/repositories/)     # Acesso a Dados
  -> SQLAlchemy / Models (app/models/)      # Mapeamento ORM
  -> SQLite (tasks.db)                      # Base de Dados Relacional

##📁 **Estrutura de Diretórios**
Plaintext
api-tarefas/
│
├── app/
│   ├── __init__.py
│   ├── main.py               # Ponto de entrada da aplicação FastAPI
│   ├── database.py           # Configuração da engine e sessão SQLAlchemy
│   ├── models/               # Modelos ORM da Base de Dados
│   ├── schemas/              # Schemas Pydantic (Request/Response DTOs)
│   ├── repositories/         # Camada de persistência e consultas
│   ├── routers/              # Endpoints e rotas HTTP da API
│   └── services/             # Lógica de negócio e serviço de IA
│
├── tests/
│   ├── test_main.py          # Testes de integração das rotas
│   └── test_ai_service.py    # Testes unitários do serviço de IA
│
├── .gitignore
├── requirements.txt
└── README.md
  
