import main

from fastapi.testclient import TestClient
# Create a TestClient instance
client = TestClient(main.app)
# Test the root endpoint  
def test_read_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"Hello": "World"}
# Test the items endpoint with query parameter          
def test_read_item():
    response = client.get("/items/5?q=priya")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": "priya"}
# Test the items endpoint without query parameter   
def test_read_item_no_query():
    response = client.get("/items/5")
    assert response.status_code == 200
    assert response.json() == {"item_id": 5, "q": None}
# Test the items endpoint with invalid item_id
def test_read_item_invalid():
    response = client.get("/items/invalid")
    assert response.status_code == 422
    assert "detail" in response.json()
# Test the items endpoint with missing item_id
def test_read_item_missing():
    response = client.get("/items/")
    assert response.status_code == 404
    assert "detail" in response.json()
# Test the items endpoint with negative item_id
def test_read_item_negative():
    response = client.get("/items/-1")
    assert response.status_code == 422
    assert "detail" in response.json()