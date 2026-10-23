from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)


def test_health_check():
  response = client.get("/health")
  assert response.status_code == 200
  data = response.json()
  assert data["status"] == "ok"
  assert "timestamp" in data


def test_create_and_list_tasks():
  # Criar uma nova tarefa
  task_data = {
      "title": "Testar a API com pytest",
      "description": "Validar o funcionamento do endpoint POST /tasks",
      "priority": "alta",
  }
  response = client.post("/tasks/", json=task_data)
  assert response.status_code == 201
  created_task = response.json()
  assert created_task["title"] == task_data["title"]
  assert created_task["id"] == 1
  assert created_task["completed"] is False

  # Listar as tarefas e verificar se a criada está lá
  response_list = client.get("/tasks/")
  assert response_list.status_code == 200
  tasks = response_list.json()
  assert len(tasks) >= 1
  assert tasks[0]["title"] == "Testar a API com pytest"
  