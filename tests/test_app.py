# test_app.py
from app import app

def test_pag_inicial():
    client = app.test_client()
    response = client.get('/')
    assert response.status_code == 200

def test_pag_2():
    client = app.test_client()
    response = client.get('/pag_2')
    assert response.status_code == 200