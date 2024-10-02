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
from django.views.decorators.http import require_http_methods
from django.utils.decorators import method_decorator
import json
from django.views.decorators.http import require_GET
import requests  # Ensure this is imported
from django.views.decorators.csrf import csrf_exempt
from django.shortcuts import render


class HomeView(ListView):
    model = Restaurant
    template_name = 'home.html'
    context_object_name = 'restaurants'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY  # If you're using Google Maps JavaScript API in templates
        return context

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY  # If you're using Google Maps JavaScript API in templates
        return context

def cuisine_list(request):
    cuisines = Cuisine.objects.all()
    context = {
        'cuisines': cuisines,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,  # If needed
    }
    return render(request, 'cuisine_list.html', context)

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

def search(request):
    query = request.GET.get('q')  
    if query:
        results = Restaurant.objects.filter(name__icontains=query)
    else:
        results = Restaurant.objects.none()  
    return render(request, 'search_results.html', {'results': results})

def home(request):
    restaurants = Restaurant.objects.all()
    cuisines = Cuisine.objects.all()
    context = {
        'restaurants': restaurants,
        'cuisines': cuisines,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,  # If needed
    }
    return render(request, 'home.html', context)

def search_results(request):
    query = request.GET.get('q')
    cuisine_id = request.GET.get('cuisine')
    restaurants = Restaurant.objects.all()

    if query:
        restaurants = restaurants.filter(
            Q(name__icontains=query) | Q(cuisine__name__icontains=query)
        )
    
    if cuisine_id:
        restaurants = restaurants.filter(cuisine_id=cuisine_id)

    context = {
        'restaurants': restaurants,
        'query': query,
        'selected_cuisine': cuisine_id,
    }
    return render(request, 'search_results.html', context)

def restaurant_detail(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    reviews = restaurant.reviews.all().order_by('-created_at')
    review_form = ReviewForm()

    context = {
        'restaurant': restaurant,
        'reviews': reviews,
        'review_form': review_form,
    }
    return render(request, 'restaurant_detail.html', context)

def add_review(request, restaurant_id):
    restaurant = get_object_or_404(Restaurant, id=restaurant_id)
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            review = form.save(commit=False)
            review.restaurant = restaurant
            review.user = request.user
            review.save()
    return redirect('restaurant_detail', restaurant_id=restaurant_id)

def filter_restaurants(request):
    if request.method == 'POST':
        cuisine = request.POST.get('cuisine')
        rating = request.POST.get('rating')

        restaurants = Restaurant.objects.all()

        if cuisine:
            restaurants = restaurants.filter(cuisine=cuisine)
        if rating:
            restaurants = restaurants.filter(rating__gte=float(rating))

        context = {'restaurants': restaurants}
        html = render_to_string('restaurant_list_partial.html', context)
        return JsonResponse({'html': html})

def restaurant_list(request):
    restaurants = Restaurant.objects.all()
    cuisines = Cuisine.objects.all()
    
    average_rating = restaurants.aggregate(Avg('rating'))['rating__avg']
    most_popular_cuisine = Cuisine.objects.annotate(
        restaurant_count=Count('restaurant')
    ).order_by('-restaurant_count').first()
    
    top_rated_restaurants = Restaurant.objects.order_by('-rating')[:6]

    context = {
        'restaurants': restaurants,
        'cuisines': cuisines,
        'average_rating': average_rating or 0,
        'most_popular_cuisine': most_popular_cuisine.name if most_popular_cuisine else 'N/A',
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,  
        'top_rated_restaurants': top_rated_restaurants,
    }
    return render(request, 'restaurant_list.html', context)

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
def search_restaurants(request):
    results = []
    error_message = None

    if request.method == 'GET' and 'query' in request.GET:
        query = request.GET.get('query')  
        location = request.GET.get('location')  
        radius = request.GET.get('radius', '3000')  
        min_rating = float(request.GET.get('min_rating', '0'))  

        if not query or not location:
            error_message = 'Query and location are required.'
        else:

            api_key = settings.GOOGLE_PLACES_API_KEY

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
                data = response.json()
                if data.get('status') != 'OK':
                    error_message = f"Error from Google Places API: {data.get('status')}"
                else:
                    results = [
                        place for place in data.get('results', [])
                        if place.get('rating', 0) >= min_rating
                    ]
            except requests.exceptions.RequestException as e:
                error_message = f"An error occurred: {str(e)}"

    context = {
        'results': results,
        'error_message': error_message,
    }
    return render(request, 'search_restaurants.html', context)

def get_restaurant_details(request):
    place_id = request.GET.get('place_id')
    error_message = None
    details = {}

    if not place_id:
        error_message = 'Place ID is required.'
    else:
        api_key = settings.GOOGLE_PLACES_API_KEY

        details_url = "https://maps.googleapis.com/maps/api/place/details/json"
        params = {
            'place_id': place_id,
            'key': api_key,
        }

        try:
            response = requests.get(details_url, params=params)
            response.raise_for_status()
            data = response.json()
            if data.get('status') != 'OK':
                error_message = f"Error from Google Places API: {data.get('status')}"
            else:
                details = data.get('result', {})
        except requests.exceptions.RequestException as e:
            error_message = f"An error occurred: {str(e)}"

    context = {
        'details': details,
        'error_message': error_message,
    }
    return JsonResponse(context)

@require_GET
def api_search_restaurants(request):
    results = []
    error_message = None

    query = request.GET.get('query')  # The search query like 'Pizza'
    location = request.GET.get('location')  # Expected format: 'lat,lng'
    radius = request.GET.get('radius', '3000')  # Default to 3000 meters
    min_rating = float(request.GET.get('min_rating', '0'))  # Default to 0

    if not query or not location:
        error_message = 'Query and location are required.'
    else:
        api_key = settings.GOOGLE_PLACES_API_KEY

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
            data = response.json()

            if data.get('status') != 'OK':
                error_message = f"Error from Google Places API: {data.get('status')}"
            else:
                results = [
                    {
                        'name': place.get('name'),
                        'rating': place.get('rating'),
                        'address': place.get('formatted_address'),
                        'place_id': place.get('place_id'),
                    }
                    for place in data.get('results', [])
                    if place.get('rating', 0) >= min_rating
                ]
        except requests.exceptions.RequestException as e:
            error_message = f"An error occurred: {str(e)}"

    if error_message:
        return JsonResponse({'error': error_message}, status=400)
    else:
        return JsonResponse({'results': results}, status=200)

def restaurant_search_page(request):
    return render(request, 'restaurants/restaurant_search.html')