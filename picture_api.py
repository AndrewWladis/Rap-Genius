import requests
import os
from dotenv import load_dotenv

def search_photo_by_name(name):
    load_dotenv()
    access_key = os.getenv('ACCESS_KEY_UNSPLASH')
    search_endpoint = 'https://api.unsplash.com/search/photos'
    
    params = {
        'query': name,
        'client_id': access_key
    }

    response = requests.get(search_endpoint, params=params)
    data = response.json()

    if 'results' in data and len(data['results']) > 0:
        photo_url = data['results'][0]['urls']['regular']
        return photo_url
    else:
        return None