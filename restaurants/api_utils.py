import requests
from django.conf import settings

def search_restaurants(query, location='33.7756,-84.3963', radius=5000):
    """Fetch nearby restaurants from Google Places API based on search query and location."""
    url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
    params = {
        'location': location,
        'radius': radius,
        'keyword': query,
        'type': 'restaurant',
        'key': settings.GOOGLE_MAPS_API_KEY,  # Make sure you have this key in your settings
    }

    response = requests.get(url, params=params)
    if response.status_code == 200:
        return response.json().get('results', [])
    return []

def get_restaurant_details(place_id):
    api_key = settings.GOOGLE_MAPS_API_KEY
    details_url = f'https://maps.googleapis.com/maps/api/place/details/json'
    params = {
        'place_id': place_id,
        'fields': 'name,rating,formatted_address,formatted_phone_number,website,opening_hours,reviews,geometry',
        'key': api_key,
    }

    response = requests.get(details_url, params=params)
    if response.status_code == 200:
        return response.json().get('result', {})
    return {}

