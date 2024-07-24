import requests

def test_get_all_data():
    url = 'http://127.0.0.1:8000/data/all'
    response = requests.get(url)
    
    # Check if the request was successful
    assert response.status_code == 200, f"Expected status code 200, got {response.status_code}"
    
    # Check the content of the response
    json_response = response.json()
    assert isinstance(json_response, dict), "Expected response to be a dictionary"
    assert "businesses" in json_response, "Expected 'businesses' key in the response"

    # Check that 'businesses' is a list
    businesses = json_response["businesses"]
    assert isinstance(businesses, list), "Expected 'businesses' to be a list"
    
    # Check the first member of the list
    assert len(businesses) > 0, "Expected 'businesses' list to have at least one item"
    first_business = businesses[0]
    assert isinstance(first_business, dict), "Expected first item in 'businesses' to be a dictionary"
    assert "name" in first_business, "Expected 'name' key in the first business"
    assert first_business["name"] == "Teton Elementary", f"Expected 'name' to be 'Teton Elementary', got {first_business['name']}"

if __name__ == "__main__":
    test_get_all_data()
