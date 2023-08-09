from django.shortcuts import render, get_object_or_404, redirect
from .models import Location, Category
from django.contrib.auth.decorators import login_required
from core.forms import *
import folium, geocoder
from profiles.models import ProfilePhoto

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
    try:
        profile_photo = ProfilePhoto.objects.get(username=request.user)
    except ProfilePhoto.DoesNotExist:
        profile_photo = None
    return render(request, 'location/place.html', {
        'similar_places' : similar_places,
        'map' : map,
        'location' : location,
        'profile_photo' : profile_photo
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
    try:
        profile_photo = ProfilePhoto.objects.get(username=request.user)
    except ProfilePhoto.DoesNotExist:
        profile_photo = None
    return render(request, 'location/contribute.html', {
        'form' : form,
        'categories' : categories,
        'heading' : 'Add a New Location to the Map',
        'profile_photo' : profile_photo
    })

@login_required
def delete(request, name):
    location = get_object_or_404(Location, name=name, created_by=request.user)
    location.delete()
    return redirect('profile')

@login_required
def edit(request, name):
    location = get_object_or_404(Location, name=name, created_by=request.user)
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
    if request.method == 'POST':
        form = EditLocation(request.POST, request.FILES, instance=location)
        if form.is_valid():
            form.save()  # Use form.save() to update the location instance
            return redirect('location:place', name=location.name)
    else:
        form = EditLocation(instance=location)
    categories = Category.objects.all()
    try:
        profile_photo = ProfilePhoto.objects.get(username=request.user)
    except ProfilePhoto.DoesNotExist:
        profile_photo = None
    return render(request, 'location/contribute.html', {
        'form': form,
        'categories': categories,
        'location': location,
        'heading': f'Edit {location.name}',
        'map' : map,
        'profile_photo' : profile_photo
    })
