from django.test import client

def test_home_status_code(client):
    response = client.get('/catalogo/lista-de-produtos')
    assert response.status_code == 200
