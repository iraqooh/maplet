from django.shortcuts import render, redirect
from location.models import *
from django.shortcuts import get_object_or_404
from location.models import Location
from .forms import *
import folium, geocoder
from geopy.geocoders import Nominatim

# Create your views here.
def index(request):
    locations = list(Location.objects.values('latitude', 'longitude'))
    latitude, longitude, search_query, heading = None, None, None, None
    if request.method == 'POST':
        form = SearchForm(request.POST)
        if form.is_valid():
            search_query = form.cleaned_data['search_query']
            geolocator = Nominatim(user_agent="my_geocoder")
            location = geolocator.geocode(search_query)
            if location:
                latitude = location.latitude
                longitude = location.longitude
                heading = f'{search_query} at {latitude:.6f}, {longitude:.2f}'
    else:
        form = SearchForm(initial={'search_query': search_query})
        heading = 'Explore Makerere University'
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'categories' : categories,
        "form" : form,
        'latitude' : latitude,
        'longitude' : longitude,
        'heading' : heading,
        'search_query' : search_query,
        'favorites' : locations
    })

def directions(request):
    location = get_object_or_404(Location, name="Main Building")
    return render(request, 'core/directions.html', {
        'location' : location
    })

def contribute(request):
    return render(request, 'core/contribute.html')

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/login/')
    else:
        form = RegistrationForm()
    return render(request, 'core/register.html', {
        'form' : form
    })

def login(request):
    return render(request, 'core/login.html')

def favorites(request):
    locations = Location.objects.all()
    categories = Category.objects.all()
    return render(request, 'core/favorites.html', {
        'locations' : locations,
        'categories' : categories,
    })

