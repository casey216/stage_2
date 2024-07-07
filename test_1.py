import os
import tempfile

import pytest


@pytest.fixture
def client():
    from app import app
    import db
    db_fd, app.config['DATABASE'] = tempfile.mkstemp()
    app.config['TESTING'] = True

    with app.test_client() as client:
        with app.app_context():
            db.init_db()
        yield client

    os.close(db_fd)
    os.unlink(app.config['DATABASE'])

def register(client, firstName, lastName, email, password, phone):
    return client.post('/auth/login', json={
        "firstName": firstName,
        "lastName": lastName,
        "email": email,
        "password": password,
        "phone": phone,
        }, follow_redirects=True)

def login(client, email, password):
    return client.post('/auth/login', json={
            "email": email,
            "password": password
            }, follow_redirects=True)


    # Access token contains correct user identity information
def test_access_token_contains_correct_user_identity_information(client):
    from flask_jwt_extended import decode_token

    response = client.post('/auth/register', json={
        "firstName": "John",
        "lastName": "Doe",
        "email": "john8.doe@example.com",
        "password": "password123",
        "phone": "1234567890"
    })

    assert response.status_code == 201
    data = response.get_json()
    assert data['status'] == 'success'
    assert 'accessToken' in data['data']

    decoded_token = decode_token(data['data']['accessToken'])
    print(decode_token)
    assert decoded_token['sub'] == 1

def test_successful_register_with_correct_email_and_password(client):
    rv = register(client, "Kenechi", "Nzewi", "caseynzewi@gmail.com", "password", "08105472526")
    assert 200 == rv.status_code
    data = rv.get_json()
    assert data["status"] == "success"

