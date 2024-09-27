from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.db.models import Q, Avg, Count
from .models import Restaurant, Cuisine, Review
from .forms import ReviewForm
from django.conf import settings
from django.http import JsonResponse
from django.template.loader import render_to_string

class HomeView(ListView):
    model = Restaurant
    template_name = 'home.html'
    context_object_name = 'restaurants'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY
        return context

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        context['google_maps_api_key'] = settings.GOOGLE_MAPS_API_KEY
        return context

def cuisine_list(request):
    cuisines = Cuisine.objects.all()
    context = {
        'cuisines': cuisines,
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY
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
        'google_maps_api_key': settings.GOOGLE_MAPS_API_KEY,
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