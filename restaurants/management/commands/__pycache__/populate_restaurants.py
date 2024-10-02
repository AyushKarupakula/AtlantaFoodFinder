# restaurants/management/commands/populate_restaurants.py

import requests
from django.core.management.base import BaseCommand, CommandError
from django.conf import settings
from restaurants.models import Restaurant, Cuisine
from django.db import IntegrityError
import logging

logger = logging.getLogger(__name__)

class Command(BaseCommand):
    help = 'Fetches restaurant data from Google Places API and populates the database.'

    def add_arguments(self, parser):
        parser.add_argument(
            '--location',
            type=str,
            help='Location to search restaurants (e.g., "Atlanta, GA")',
            default='Atlanta, GA'
        )
        parser.add_argument(
            '--radius',
            type=int,
            help='Search radius in meters (max 50000)',
            default=50000
        )
        parser.add_argument(
            '--type',
            type=str,
            help='Type of place to search (e.g., "restaurant")',
            default='restaurant'
        )

    def handle(self, *args, **options):
        location = options['location']
        radius = options['radius']
        place_type = options['type']

        if radius > 50000:
            self.stderr.write(self.style.ERROR('Radius cannot exceed 50,000 meters.'))
            return

        self.stdout.write(self.style.NOTICE(f'Searching for {place_type}s in {location} within {radius} meters.'))

        # Geocoding to get latitude and longitude of the location
        geocode_url = 'https://maps.googleapis.com/maps/api/geocode/json'
        geocode_params = {
            'address': location,
            'key': settings.GOOGLE_PLACES_API_KEY
        }

        response = requests.get(geocode_url, params=geocode_params)
        if response.status_code != 200:
            raise CommandError(f'Geocoding API request failed with status {response.status_code}.')

        geocode_data = response.json()
        if not geocode_data['results']:
            raise CommandError('No geocoding results found for the provided location.')

        location_coords = geocode_data['results'][0]['geometry']['location']
        lat = location_coords['lat']
        lng = location_coords['lng']

        self.stdout.write(self.style.SUCCESS(f'Location coordinates: ({lat}, {lng})'))

        # Places API to search for restaurants
        places_url = 'https://maps.googleapis.com/maps/api/place/nearbysearch/json'
        places_params = {
            'location': f'{lat},{lng}',
            'radius': radius,
            'type': place_type,
            'key': settings.GOOGLE_PLACES_API_KEY
        }

        while True:
            places_response = requests.get(places_url, params=places_params)
            if places_response.status_code != 200:
                raise CommandError(f'Places API request failed with status {places_response.status_code}.')

            places_data = places_response.json()

            if places_data.get('status') != 'OK' and places_data.get('status') != 'ZERO_RESULTS':
                raise CommandError(f'Places API error: {places_data.get("status")}, {places_data.get("error_message")}')

            results = places_data.get('results', [])
            if not results:
                self.stdout.write(self.style.WARNING('No more results found.'))
                break

            for place in results:
                try:
                    name = place.get('name')
                    address = place.get('vicinity') or place.get('formatted_address')
                    latitude = place['geometry']['location']['lat']
                    longitude = place['geometry']['location']['lng']
                    rating = place.get('rating', 0.0)
                    place_id = place.get('place_id')

                    # Get cuisine type from types or keyword (simplistic approach)
                    types = place.get('types', [])
                    cuisine_name = 'Unknown'
                    if 'cuisine' in types:
                        # This is unlikely; better to use keywords or additional API calls
                        cuisine_name = 'Cuisine'
                    else:
                        # Attempt to extract cuisine from types
                        for t in types:
                            if t in ['italian', 'mexican', 'chinese', 'japanese', 'indian', 'french', 'thai', 'vietnamese']:
                                cuisine_name = t.capitalize()
                                break

                    # Get or create Cuisine
                    cuisine, created = Cuisine.objects.get_or_create(name=cuisine_name)

                    # Create or update Restaurant
                    restaurant, created = Restaurant.objects.update_or_create(
                        place_id=place_id,
                        defaults={
                            'name': name,
                            'cuisine': cuisine,
                            'address': address,
                            'latitude': latitude,
                            'longitude': longitude,
                            'rating': rating,
                            # 'image': '',  # Images require separate handling
                            'description': '',  # Optional
                        }
                    )

                    if created:
                        self.stdout.write(self.style.SUCCESS(f'Added restaurant: {name}'))
                    else:
                        self.stdout.write(self.style.NOTICE(f'Updated restaurant: {name}'))

                except IntegrityError as e:
                    logger.error(f'IntegrityError for place {place.get("place_id")}: {e}')
                    continue
                except Exception as e:
                    logger.error(f'Unexpected error for place {place.get("place_id")}: {e}')
                    continue

            # Handle pagination with next_page_token
            next_page_token = places_data.get('next_page_token')
            if next_page_token:
                import time
                time.sleep(2)  # Required delay before using next_page_token
                places_params = {
                    'pagetoken': next_page_token,
                    'key': settings.GOOGLE_PLACES_API_KEY
                }
            else:
                break

        self.stdout.write(self.style.SUCCESS('Restaurant data population complete.'))
