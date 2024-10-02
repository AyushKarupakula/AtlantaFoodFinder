import os
import requests

def search_restaurants():
    # Replace 'YOUR_API_KEY' with your actual Google Places API key
    api_key = 'AIzaSyDybEBTmKfVLpRvWEjxzDp6rstLh_IQAvE'

    # Search parameters
    query = 'Pizza'  # Change to your desired search term
    location = '33.7490,-84.3880'  # Change to your desired location (latitude,longitude)
    radius = '3000'  # Search radius in meters
    min_rating = 0  # Minimum rating filter

    # Construct the URL for Places Text Search API
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

    # Check for API errors
    if data.get('status') != 'OK':
        print(f"Error from Google Places API: {data.get('status')}")
        print(data.get('error_message', ''))
        return

    # Filter results by minimum rating
    results = [
        place for place in data.get('results', [])
        if place.get('rating', 0) >= min_rating
    ]

    # Print the results
    for place in results:
        print(f"Name: {place['name']}")
        print(f"Rating: {place.get('rating', 'N/A')}")
        print(f"Address: {place.get('formatted_address', 'N/A')}")
        print(f"Place ID: {place['place_id']}")
        print('---')

if __name__ == '__main__':
    search_restaurants()
