# views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, Count
from .models import Restaurant, Cuisine, Review
from .forms import ReviewForm
from django.conf import settings
from django.http import JsonResponse
from django.template.loader import render_to_string
from django.core.serializers import serialize
from django.http import HttpResponse
from .models import Restaurant, Favorite
import requests
from .api_utils import search_restaurants, get_restaurant_details

# Class-based view for home page
class HomeView(ListView):
    model = Restaurant
    template_name = 'home.html'
    context_object_name = 'restaurants'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY  # If you're using Google Maps JavaScript API in templates
        return context
def home(request):
    """Home view to display all restaurants and cuisines."""
    restaurants = Restaurant.objects.all()
    cuisines = Cuisine.objects.all()
    context = {
        'restaurants': restaurants,
        'cuisines': cuisines,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
    }
    return render(request, 'home.html', context)


# Function-based view to list all cuisines
def cuisine_list(request):
    cuisines = Cuisine.objects.all()
    context = {
        'cuisines': cuisines,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,  # If needed
    }
    return render(request, 'cuisine_list.html', context)

# Function-based view to list restaurants by cuisine
def restaurant_by_cuisine(request, cuisine_id):
    cuisine = get_object_or_404(Cuisine, pk=cuisine_id)
    restaurants = Restaurant.objects.filter(cuisine=cuisine)
    return render(request, 'restaurant_by_cuisine.html', {'cuisine': cuisine, 'restaurants': restaurants})

@login_required
def add_review(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()
    return redirect('restaurant_detail', pk=pk)

@login_required
def toggle_favorite(request, pk):
    restaurant = get_object_or_404(Restaurant, pk=pk)
    user = request.user
    if restaurant in user.favorite_restaurants.all():
        user.favorite_restaurants.remove(restaurant)
    else:
        user.favorite_restaurants.add(restaurant)
    return redirect('restaurant_detail', pk=pk)


def restaurant_search(request):
    # Retrieve the search query and cuisine from the GET parameters
    query = request.GET.get('q', '')  # Get the search query from the user input

    selected_cuisine = request.GET.get('cuisine', '')

    # If a query exists, use the search function to get results

    if query:
        restaurants = search_restaurants(query)
        return render(request, 'search_results.html', {
            'restaurants': restaurants,
            'query': query,
            'selected_cuisine': selected_cuisine,
        })
    # Return an empty search results page if no query is provided
    return render(request, 'search_results.html', {
        'restaurants': [],
        'query': query,
        'selected_cuisine': selected_cuisine,
    })


# Function-based view to display detailed information of a restaurant using place_id
# views.py

def restaurant_detail(request, place_id):
    # Fetch restaurant details using the API
    restaurant_details = get_restaurant_details(place_id)  # Modify this function if necessary

    # Check if the details contain the latitude and longitude
    latitude = restaurant_details.get('geometry', {}).get('location', {}).get('lat')
    longitude = restaurant_details.get('geometry', {}).get('location', {}).get('lng')

    context = {
        'restaurant': {
            'name': restaurant_details.get('name'),
            'formatted_address': restaurant_details.get('formatted_address'),
            'formatted_phone_number': restaurant_details.get('formatted_phone_number'),
            'website': restaurant_details.get('website'),
            'rating': restaurant_details.get('rating'),
            'opening_hours': restaurant_details.get('opening_hours'),
            'latitude': latitude,  # Add latitude
            'longitude': longitude,  # Add longitude
        },
        'reviews': restaurant_details.get('reviews', []),
        'place_id': place_id,
        'query': request.GET.get('q', ''),
        'selected_cuisine': request.GET.get('cuisine', ''),
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,  # Ensure this is in your settings.py
    }

    return render(request, 'restaurant_detail.html', context)



# Function-based view to list all restaurants
def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    cuisines = Cuisine.objects.all()
    
    # Serialize restaurant data to JSON for use in JavaScript
    restaurant_data = serialize('json', restaurants, fields=('id', 'name', 'latitude', 'longitude'))

    context = {
        'restaurants': restaurant_data,
        'cuisines': cuisines,

        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,

    }
    return render(request, 'restaurant_list.html', context)

# API endpoint to get all restaurant data in JSON format
def restaurant_api(request):
    restaurants = Restaurant.objects.all()
    data = [{
        'id': restaurant.id,
        'name': restaurant.name,
        'latitude': restaurant.latitude,
        'longitude': restaurant.longitude,
        'rating': restaurant.rating,
        'cuisine': restaurant.cuisine.name if restaurant.cuisine else ''
    } for restaurant in restaurants]
    return JsonResponse(data, safe=False)

# Function to get reviews from Google
def fetch_google_reviews(restaurant_name, restaurant_address):
    google_places_url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json'
    params = {
        'input': f'{restaurant_name} {restaurant_address}',
        'inputtype': 'textquery',
        'fields': 'place_id',
        'key': settings.GOOGLE_MAPS_API_KEY,
    }

    response = requests.get(google_places_url, params=params)
    if response.status_code == 200 and response.json().get('candidates'):
        place_id = response.json()['candidates'][0]['place_id']
        
        # Fetch details including reviews
        details_url = f'https://maps.googleapis.com/maps/api/place/details/json'
        details_params = {
            'place_id': place_id,
            'fields': 'reviews',
            'key': settings.GOOGLE_MAPS_API_KEY,
        }
        details_response = requests.get(details_url, params=details_params)
        if details_response.status_code == 200:
            return details_response.json().get('result', {}).get('reviews', [])
    return []

def search_results(request):
    query = request.GET.get('q', '')  # Get the search query from the user input
    cuisine_id = request.GET.get('cuisine', '')
    
    # Use the search_restaurants function to search using the Google Places API
    if query:
        restaurants = search_restaurants(query)
        return render(request, 'search_results.html', {'restaurants': restaurants, 'query': query, 'selected_cuisine': cuisine_id})

    return render(request, 'search_results.html', {'restaurants': [], 'query': query, 'selected_cuisine': cuisine_id})


def add_to_favorites(request, place_id):
    restaurant = get_object_or_404(Restaurant, place_id=place_id)
    Favorite.objects.get_or_create(user=request.user, restaurant=restaurant)
    return redirect('restaurant_detail', place_id=place_id)

# Remove restaurant from favorites
@login_required
def remove_from_favorites(request, place_id):
    restaurant = get_object_or_404(Restaurant, place_id=place_id)
    favorite = Favorite.objects.filter(user=request.user, restaurant=restaurant)
    if favorite.exists():
        favorite.delete()
    return redirect('restaurant_detail', place_id=place_id)

# View to list all favorite restaurants
@login_required
def view_favorites(request):
    favorites = Favorite.objects.filter(user=request.user).select_related('restaurant')
    context = {'favorites': favorites}
    return render(request, 'view_favorites.html', context)  