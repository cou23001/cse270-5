# data_fetcher.py

import requests

def fetch_data(url):
    response = requests.get(url)
    data = response.json()
    return data['key']  # Return the value associated with 'key' in the JSON response
