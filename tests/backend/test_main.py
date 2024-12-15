from app.backend.main import main
from fastapi.testclient import TestClient
from app.backend.main import app, messages_list

client = TestClient(app)

def test_read_main():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"message": "Hello"}

def test_about():
    response = client.get("/about")
    assert response.status_code == 200
    assert response.json() == {"message": "This is the about page."}

def test_add_msg():
    response = client.post("/messages/test_message/")
    assert response.status_code == 200
    assert response.json() == {"message": "test_message"}
    assert 0 in messages_list
    assert messages_list[0] == "test_message"

def test_message_items():
    client.post("/messages/test_message/")
    response = client.get("/messages")
    assert response.status_code == 200
    assert "messages" in response.json()
    assert "test_message" in response.json()["messages"].values()

def test_ingest_data_route():
    response = client.post("/ingest_data/")
    assert response.status_code == 200
    assert response.json() == {"message": "Data ingestion completed"}

def test_train_model_route():
    response = client.post("/train_model/")
    assert response.status_code == 200
    assert response.json() == {"message": "Model training completed"}

def test_generate_predictions_route():
    response = client.post("/generate_predictions/")
    assert response.status_code == 200
    assert response.json() == {"message": "Predictions generated"}

def test_communicate_route():
    response = client.post("/communicate/")
    assert response.status_code == 200
    assert response.json() == {"message": "Communication completed"}
