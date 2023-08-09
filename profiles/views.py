from django.shortcuts import render, get_object_or_404
from location.models import Location
from .models import ProfilePhoto
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request):
    contributions = Location.objects.filter(created_by=request.user)
    try:
        profile_photo = ProfilePhoto.objects.get(username=request.user)
    except ProfilePhoto.DoesNotExist:
        profile_photo = None
    success = request.session.pop('success', None)
    return render(request, 'core/profile.html', {
        'contributions' : contributions,
        'user' : request.user,
        'success' : success,
        'profile_photo' : profile_photo
    })

