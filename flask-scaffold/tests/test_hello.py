from app import app

def test_index_route():
    response = app.test_client().get('/')
    assert response.data == b'<h1>Hello, World!</h1>'