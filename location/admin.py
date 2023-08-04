from django.contrib import admin
from .models import Category, Location

# Register your models here.
admin.site.register((Category, Location))