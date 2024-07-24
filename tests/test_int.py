import requests
import pytest


@pytest.fixture
def credentials():
    return {
        'username': 'admin',
        'password': 'qwerty'
    }

def test_user_login_success(credentials):
    url = f"http://127.0.0.1:8000/users/?username=}&password={credentials['password']}"
    response = requests.get(url)
    
    # Check if the request was successful
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Check the content of the response (expected to be empty)
    assert response.text == "", "Expected response to be empty"
    