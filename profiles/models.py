from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class ProfilePhoto(models.Model):
    image = models.ImageField(default='images/no_profile_image.png', upload_to='media')
    username = models.ForeignKey(User, on_delete=models.CASCADE, related_name='profilephotos')
    def __str__(self):
        return self.image