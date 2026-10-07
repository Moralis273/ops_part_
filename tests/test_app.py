from app import app

def test_health():
    client=app.test_client()
    response=client.get("/health")
    assert response.status_code ==200
    assert response.get_json()=={"status":"ok"}
    
def test_predict():
    client=app.test_client()
    response=client.post("/predict",json={"age":40, "purchase_amount":300})
    data=response.get_json()
    assert response.status_code==200
    assert "probability" in data
    assert 0<=data["probability"]<=1
    