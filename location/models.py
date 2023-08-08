from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=255)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Categories'

    def __str__(self):
        return self.name
    
class Location(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, default='Lecture Building', related_name='locations', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()
    image = models.ImageField(upload_to='media', blank=True, null=True)
    created_by = models.ForeignKey(User, related_name='locations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ('name',)
        verbose_name_plural = 'Locations'

    def __str__(self):
        return self.name

class Navigation(models.Model):
    start = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='start_navigations')
    destination = models.ForeignKey(Location, on_delete=models.CASCADE, related_name='destination_navigations')
    created_by = models.ForeignKey(User, related_name='navigations', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.start.name} to {self.destination.name}'