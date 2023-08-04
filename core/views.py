from django.shortcuts import render, redirect
from location.models import *
from django.shortcuts import get_object_or_404
from location.models import Location
from .forms import RegistrationForm
import folium, geocoder

# Create your views here.
def index(request):
    map = folium.Map(
        location=[0.332882, 32.568594],
        zoom_start=17,
        height="50%",
        width="75%"
    )
    folium.Marker(
        [0.332691, 32.568596],
        tooltip='Click for more', popup='Makerere University'
    ).add_to(map)
    # folium.Marker(
    #     [lat, lng],
    #     tooltip='Click for more', popup=country
    # ).add_to(map)
    map = map._repr_html_()
    location = get_object_or_404(Location, name="Main Building")
    categories = Category.objects.all()
    return render(request, 'core/index.html', {
        'location' : location,
        'categories' : categories,
        "map" : map,
        # "form" : form
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

