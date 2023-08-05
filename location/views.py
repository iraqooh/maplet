from django.shortcuts import render, get_object_or_404, redirect
from .models import Location, Category
from django.contrib.auth.decorators import login_required
from core.forms import *

# Create your views here.
def place(request, name):
    location = get_object_or_404(Location, name=name)
    similar_places = Location.objects.filter(category=location.category).exclude(name=name)[0:3]
    return render(request, 'location/place.html', {
        'location' : location,
        'similar_places' : similar_places
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