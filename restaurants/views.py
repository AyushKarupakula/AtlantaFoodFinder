from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from .models import Restaurant, Cuisine, Review
from .forms import ReviewForm
from django.conf import settings

class HomeView(ListView):
    model = Restaurant
    template_name = 'home.html'
    context_object_name = 'restaurants'

class RestaurantDetailView(DetailView):
    model = Restaurant
    template_name = 'restaurant_detail.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['review_form'] = ReviewForm()
        return context

def cuisine_list(request):
    cuisines = Cuisine.objects.all()
    return render(request, 'cuisine_list.html', {'cuisines': cuisines})

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
    top_restaurants = Restaurant.objects.order_by('-rating')[:6]
    cuisines = Cuisine.objects.all()
    context = {
        'top_restaurants': top_restaurants,
        'cuisines': cuisines,
        'GOOGLE_MAPS_API_KEY': settings.GOOGLE_MAPS_API_KEY,
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