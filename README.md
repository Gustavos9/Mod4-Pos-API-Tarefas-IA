# Micro-API de Gerenciamento de Tarefas

API RESTful desenvolvida em **Python** e **FastAPI** para o gerenciamento de tarefas (To-Do List), contando com persistência de dados em base relacional e recursos avançados de arquitetura.

---

## 🚀 Visão Geral
O núcleo utiliza **Pydantic** para validação de dados, **SQLAlchemy** para persistência e **SQLite** em arquivo como base de dados padrão. A aplicação está estruturada em camadas, garantindo baixo acoplamento, alta coesão e testabilidade.

## 🛠️ Tecnologias Utilizadas
* **Python 3.12+**
* **FastAPI** (Framework web assíncrono e de alta performance)
* **SQLAlchemy** (ORM para mapeamento objeto-relacional)
* **SQLite** (Base de dados relacional leve e persistente)
* **Pydantic V2** (Validação de schemas e DTOs)
* **Pytest** (Suíte de testes automatizados)

---

## 📋 Funcionalidades Implementadas
- **CRUD Completo:** Criação, listagem, consulta por ID, atualização parcial (`PATCH`) e exclusão de tarefas.
- **Gestão de Estados:** Conclusão de tarefas por status (`pending` / `completed`).
- **Filtros Dinâmicos:** Filtragem de tarefas por parâmetros de consulta (`query parameters`).
- **Persistência Real:** Os dados persistem num ficheiro local (`tasks.db`) mesmo após reiniciar a aplicação.
- **Validação Robusta:** Respostas HTTP padronizadas (`201 Created`, `200 OK`, `404 Not Found`, `422 Unprocessable Entity`).
- **Health Check:** Endpoint dedicado em `/health`.
- **Documentação Automática:** Swagger UI interativo disponível em `/docs`.
- **Serviço de IA Opcional:** Módulo de priorização automática de tarefas com heurística local e normalização de acentos.

---

## 🏛️ Arquitetura do Projeto
A aplicação segue uma arquitetura limpa em camadas:
