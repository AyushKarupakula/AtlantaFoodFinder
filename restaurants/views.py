from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView
from django.contrib.auth.decorators import login_required
from .models import Restaurant, Cuisine, Review
from .forms import ReviewForm

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