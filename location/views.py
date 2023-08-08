from django.shortcuts import render, get_object_or_404, redirect
from .models import Location, Category
from django.contrib.auth.decorators import login_required
from core.forms import *
import folium, geocoder

# Create your views here.
def place(request, name):
    location = get_object_or_404(Location, name=name)
    map = folium.Map(
        location=[location.latitude, location.longitude],
        zoom_start=17
    )
    country = geocoder.osm(location.name).country
    folium.Marker(
        location=[location.latitude, location.longitude],
        tooltip=location.name,
        popup=f'{location.name}\n{location.latitude}, {location.longitude}\n{country}'
    ).add_to(map)
    
    map = map._repr_html_()
    similar_places = Location.objects.filter(category=location.category).exclude(name=name)[0:3]
    return render(request, 'location/place.html', {
        'similar_places' : similar_places,
        'map' : map,
        'location' : location
    })

@login_required
def contribute(request):
    if request.method == 'POST':
        form = Contribution(request.POST, request.FILES)
        if form.is_valid():
            location = form.save(commit=False)
            location.created_by = request.user
            location.save()
            return redirect('location:place', name=location.name)
    else: form = Contribution()
    categories = Category.objects.all()
    location = get_object_or_404(Location, name='Main Building')
    return render(request, 'location/contribute.html', {
        'form' : form,
        'categories' : categories,
        'location' : location,
        'heading' : 'Add a New Location to the Map'
    })

@login_required
def delete(request, name):
    location = get_object_or_404(Location, name=name, created_by=request.user)
    location.delete()
    return redirect('profile')

@login_required
def edit(request, name):
    location = get_object_or_404(Location, name=name, created_by=request.user)
    if request.method == 'POST':
        form = EditLocation(request.POST, request.FILES, instance=location)
        if form.is_valid():
            location.save()
            return redirect('location:place', name=location.name)
    else: form = EditLocation(instance=location)
    categories = Category.objects.all()
    location = get_object_or_404(Location, name='Main Building')
    return render(request, 'location/contribute.html', {
        'form' : form,
        'categories' : categories,
        'location' : location,
        'heading' : f'Edit {location.name}'
    })