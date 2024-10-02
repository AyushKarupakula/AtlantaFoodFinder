import os
import requests

def search_restaurants():
    api_key = 'AIzaSyDybEBTmKfVLpRvWEjxzDp6rstLh_IQAvE'

    # Search parameters
    query = 'Pizza'  
    location = '33.7490,-84.3880'  
    radius = '3000'  
    min_rating = 0 

    places_url = "https://maps.googleapis.com/maps/api/place/textsearch/json"
    params = {
        'query': query,
        'location': location,
        'radius': radius,
        'key': api_key,
    }

    try:
        response = requests.get(places_url, params=params)
        response.raise_for_status()
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")
        return

    data = response.json()

    if data.get('status') != 'OK':
        print(f"Error from Google Places API: {data.get('status')}")
        print(data.get('error_message', ''))
        return

    results = [
        place for place in data.get('results', [])
        if place.get('rating', 0) >= min_rating
    ]

    for place in results:
        print(f"Name: {place['name']}")
        print(f"Rating: {place.get('rating', 'N/A')}")
        print(f"Address: {place.get('formatted_address', 'N/A')}")
        print(f"Place ID: {place['place_id']}")
        print('---')

if __name__ == '__main__':
    search_restaurants()
