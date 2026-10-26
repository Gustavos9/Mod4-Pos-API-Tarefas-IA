# Documentação da API de Tarefas
# 📚 Visão Geral do Projeto (Overview)

Este documento apresenta a arquitetura, o propósito e a estrutura técnica da **API RESTful de Gerenciamento de Tarefas com FastAPI e IA**.

---

## 🎯 Propósito do Projeto
Desenvolvido como parte do laboratório prático de pós-graduação, este MVP (*Minimum Viable Product*) tem como objetivo fornecer um microsserviço de gestão de tarefas (To-Do List) robusto, escalável e de fácil manutenção, aplicando as melhores práticas de desenvolvimento backend em Python.

---

## 🏗️ Arquitetura e Decisões de Design
O projeto adota rigorosamente uma **Arquitetura em Camadas (Layered Architecture)** para garantir a separação de responsabilidades (*Separation of Concerns*) e facilitar a testabilidade:

1. **Camada de Apresentação (`app/routers/`):** Controla os endpoints HTTP, recebe as requisições, delega o processamento e devolve respostas padronizadas.
2. **Camada de Regras de Negócio (`app/services/`):** Concentra a lógica da aplicação, incluindo o motor de processamento e priorização inteligente de tarefas.
3. **Camada de Acesso a Dados (`app/repositories/` e `app/models/`):** Gerencia a persistência relacional utilizando **SQLAlchemy** e mapeamento ORM, suportando SQLite em ficheiro local para produção/desenvolvimento e em memória para testes.
4. **Validação de Dados (`app/schemas/`):** Utiliza **Pydantic V2** para garantir a tipagem estrita e a integridade dos dados de entrada e saída.

---

## 💡 Módulo de Inteligência Artificial
O sistema conta com um componente de serviços dedicado à IA (`AITaskService`). Este módulo analisa o conteúdo textual das tarefas (títulos e descrições), aplicando normalização de caracteres e heurísticas para sugerir ou ajustar automaticamente os níveis de prioridade de forma inteligente.

---

## 🧪 Estratégia de Testes
A qualidade e a fiabilidade do código são garantidas por uma suíte de testes automatizados desenvolvida com **Pytest**, executada num ambiente completamente isolado (`sqlite:///:memory:`), assegurando que os testes não afetam a base de dados local (`tasks.db`).