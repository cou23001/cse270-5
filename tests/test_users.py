import requests


def test_user_login_success():
    url = "http://127.0.0.1:8000/users/?username=admin&password=qwerty"    
    response = requests.get(url)
    
    # Check if the request was successful
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Check the content of the response (expected to be empty)
    assert response.text == "", "Expected response to be empty"


def test_user_login_unsuccess():
    url = "http://127.0.0.1:8000/users/?username=admin&password=admin"    
    response = requests.get(url)
    
    # Check if the request was successful
    assert response.status_code == 401, f"Expected status code 401, got {response.status_code}"
    
    # Check the content of the response (expected to be empty)
    assert response.text == "", "Expected response to be empty"


