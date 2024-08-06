import requests
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('API_KEY')

# Asteroids by ID
def get_asteroid_by_id(asteroid_id, api_key):
    """
    Lookup a specific asteroid based on its NASA JPL small body (SPK-ID) ID.
    
    :param asteroid_id: NASA JPL small body (SPK-ID) ID of the asteroid.
    :param api_key: NASA API key (default is DEMO_KEY).
    :return: JSON response from the API.
    """
    url = f"https://api.nasa.gov/neo/rest/v1/neo/{asteroid_id}"
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

# Asteroids by date
def get_asteroids_by_date(start_date, end_date, api_key):
    """
    Retrieve a list of asteroids based on their closest approach date to Earth.
    
    :param start_date: Start date for asteroid search in YYYY-MM-DD format.
    :param end_date: End date for asteroid search in YYYY-MM-DD format.
    :param api_key: NASA API key (default is API_KEY).
    :return: JSON response from the API.
    """
    url = f"https://api.nasa.gov/neo/rest/v1/feed"
    params = {
        'start_date': start_date,
        'end_date': end_date,
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    return response.json()

# Browse asteroids dataset
def browse_asteroid_dataset(api_key):
    """
    Browse the overall asteroid data-set.
    
    :param api_key: NASA API key (default is API_KEY).
    :return: JSON response from the API.
    """
    url = "https://api.nasa.gov/neo/rest/v1/neo/browse/"
    params = {
        'api_key': api_key
    }
    response = requests.get(url, params=params)
    return response.json()
