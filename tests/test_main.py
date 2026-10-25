from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

def test_health_check():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json()["status"] == "ok"

def test_create_list_and_filter_tasks():
    resp1 = client.post("/tasks/", json={"title": "Erro urgente em producao"})
    assert resp1.status_code == 201
    
    resp2 = client.post("/tasks/", json={"title": "Comprar cafe"})
    assert resp2.status_code == 201

    all_tasks = client.get("/tasks/").json()
    assert len(all_tasks) >= 2

    high_tasks = client.get("/tasks/?priority=alta").json()
    assert all(t["priority"] == "alta" for t in high_tasks)

def test_update_task_status():
    create_resp = client.post("/tasks/", json={"title": "Ajuste na reuniao"})
    task_id = create_resp.json()["id"]

    patch_resp = client.patch(f"/tasks/{task_id}", json={"completed": True})
    assert patch_resp.status_code == 200
    assert patch_resp.json()["completed"] is True

    notFound_resp = client.patch("/tasks/9999", json={"completed": True})
    assert notFound_resp.status_code == 404
