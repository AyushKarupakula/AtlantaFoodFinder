import os
import requests

def get_restaurant_details():
    # Replace 'YOUR_API_KEY' with your actual Google Places API key
    api_key = 'AIzaSyDybEBTmKfVLpRvWEjxzDp6rstLh_IQAvE'  # <-- Enter your API key here

    # Replace 'YOUR_PLACE_ID' with the place ID of the restaurant you want details for
    place_id = 'ChIJB-a9NO0E9YgRRTE_-m4Xrzo'  # <-- Enter the place ID here

    # Construct the URL for Place Details API
    details_url = "https://maps.googleapis.com/maps/api/place/details/json"
    params = {
        'place_id': place_id,
        'key': api_key,
    }

    try:
        response = requests.get(details_url, params=params)
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

    details = data.get('result', {})

    # Print detailed information
    print(f"Name: {details.get('name', 'N/A')}")
    print(f"Phone Number: {details.get('formatted_phone_number', 'N/A')}")
    print(f"Website: {details.get('website', 'N/A')}")
    print(f"Address: {details.get('formatted_address', 'N/A')}")
    print(f"Rating: {details.get('rating', 'N/A')}")
    print("Opening Hours:")
    opening_hours = details.get('opening_hours', {}).get('weekday_text', [])
    if opening_hours:
        for day in opening_hours:
            print(f"  {day}")
    else:
        print("  N/A")

if __name__ == '__main__':
    get_restaurant_details()
