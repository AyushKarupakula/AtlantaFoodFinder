import os
import requests

def get_restaurant_details():
    api_key = 'AIzaSyDybEBTmKfVLpRvWEjxzDp6rstLh_IQAvE'  

    place_id = 'ChIJB-a9NO0E9YgRRTE_-m4Xrzo'  

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

    if data.get('status') != 'OK':
        print(f"Error from Google Places API: {data.get('status')}")
        print(data.get('error_message', ''))
        return

    details = data.get('result', {})

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
