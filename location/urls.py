from django.urls import path
from . import views

app_name = 'location'

urlpatterns = [
    path('contribute/', views.contribute, name='contribute'),
    path('<str:name>/', views.place, name='place'),
    path('<str:name>/delete/', views.delete, name='delete'),
    path('<str:name>/edit', views.edit, name='edit')
]