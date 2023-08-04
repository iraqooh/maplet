from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from location.models import Location, Category

class RegistrationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
        
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter your username...',
        'class' : 'w-full px-3 py-3 rounded-xl',
    }))
    email = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter email...',
        'class' : 'w-full px-3 py-3 rounded-xl'
    }))
    password1 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter a strong password...',
        'class' : 'w-full px-3 py-3 rounded-xl',
        'type' : 'password'
    }))
    password2 = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Repeat the password...',
        'class' : 'w-full px-3 py-3 rounded-xl',
        'type' : 'password'
    }))

class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter your username...',
        'class' : 'w-full px-3 py-3 rounded-xl'
    }))
    password = forms.CharField(widget=forms.TextInput(attrs={
        'placeholder' : 'Enter a strong password...',
        'class' : 'w-full px-3 py-3 rounded-xl',
        'type' : 'password'
    }))

INPUT_CLASSES = 'w-full px-3 py-3 rounded-xl'

class Contribution(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'category', 'latitude', 'longitude', 'image',)
        widgets = {
            'category' : forms.Select(attrs={
                'class' : INPUT_CLASSES
            }),
            'name' : forms.TextInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'latitude' : forms.NumberInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'longitude' : forms.NumberInput(attrs={
                'class' : INPUT_CLASSES
            }),
            'image' : forms.FileInput(attrs={
                'class' : INPUT_CLASSES
            })
        }
    # name = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder' : 'Enter name...',
    #     'class' : 'w-full px-3 py-3 rounded-xl',
    # }))
    # category = forms.CharField(widget=forms.TextInput(attrs={
    #     'placeholder' : 'Select the category...',
    #     'class' : 'w-full px-3 py-3 rounded-xl',
    # }))
    # latitude = forms.FloatField(widget=forms.TextInput(attrs={
    #     'placeholder' : 'Enter the latitude or select a point on the map...',
    #     'class' : 'w-full px-3 py-3 rounded-xl',
    # }))
    # longitude = forms.FloatField(widget=forms.TextInput(attrs={
    #     'placeholder' : 'Enter the longitude or select a point on the map...',
    #     'class' : 'w-full px-3 py-3 rounded-xl',
    # }))
    # image = forms.ImageField(widget=forms.ImageField())
