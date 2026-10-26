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
```

---

## ⚙️ Configuração e Execução Local

### 1. Ambiente Virtual
No terminal (PowerShell), crie e ative o ambiente virtual:

```powershell
python -m venv .venv
.venv\Scripts\Activate.ps1
```
2. Instalação das Dependências
```PowerShell
python -m pip install --upgrade pip
pip install -r requirements.txt
```
3. Executando a API
```PowerShell
uvicorn app.main:app --reload
```
Acesse a documentação interativa em http://127.0.0.1:8000/docs.

---

### 🧪 Suíte de Testes Automatizados
```
Para certificar a integridade do sistema, execute os testes com o pytest num ambiente isolado:

PowerShell
PYTHONPATH=. pytest -v

A suíte abrange validações de schemas, regras de negócio, testes de integração das rotas HTTP e comportamento do repositório.

```
---

## 📌 Endpoints da API

| Método | Rota | Status de Sucesso | Descrição |
| :--- | :--- | :--- | :--- |
| **POST** | `/tasks` | `201 Created` | Regista uma nova tarefa no sistema. |
| **GET** | `/tasks` | `200 OK` | Retorna a lista de tarefas (com suporte a filtros). |
| **GET** | `/tasks/{task_id}` | `200 OK` | Consulta os detalhes de uma tarefa específica. |
| **PATCH** | `/tasks/{task_id}` | `200 OK` | Atualiza atributos ou o status de conclusão. |
| **DELETE** | `/tasks/{task_id}` | `204 No Content` | Remove permanentemente a tarefa especificada. |
| **GET** | `/health` | `200 OK` | Retorna o estado operacional do microsserviço. |
---
*Desenvolvido por **Gustavo Sabino** / **Lucas Ferreira** para avaliação de Pós-Graduação.*
