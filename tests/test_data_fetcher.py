# test_data_fetcher.py

import pytest
import requests
from data_fetcher import fetch_data

def test_fetch_data(mocker):
    # Define the mock response data
    mock_response = mocker.Mock()
    mock_response.json.return_value = {'key': 'mocked_value'}
    
    # Patch 'requests.get' to return the mock response
    mocker.patch('requests.get', return_value=mock_response)
    
    # Call the function
    result = fetch_data('http://fakeurl.com/api/data')
    
    # Assert that the function returns the mocked value
    assert result == 'mocked_value'
    
    # Optionally check that requests.get was called with the correct URL
    requests.get.assert_called_once_with('http://fakeurl.com/api/data')
