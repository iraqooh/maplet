from django.shortcuts import render, get_object_or_404
from location.models import Location
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def profile(request):
    contributions = Location.objects.filter(created_by=request.user)
    return render(request, 'core/profile.html', {
        'contributions' : contributions,
        'user' : request.user
    })

