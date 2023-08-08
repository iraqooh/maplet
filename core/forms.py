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

class EditLocation(forms.ModelForm):
    class Meta:
        model = Location
        fields = ('name', 'category', 'latitude', 'longitude', 'image',)
        widgets = {
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

class SearchForm(forms.Form):
    search_query = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Search...',
            'label' : '',
            'name' : 'query',
            'class' : "p-2 rounded-xl",
            'z-index' : '2'
        })
    )

class NavigationForm(forms.Form):
    source = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Choose starting point, or click on the map...',
            'label' : '',
            'name' : 'source',
            'class' : "form-control w-3/4 p-2 mb-4 rounded-xl",
        })
    )
    destination = forms.CharField(
        max_length=100,
        widget=forms.TextInput(attrs={
            'placeholder': 'Choose destination...',
            'label' : '',
            'name' : 'destination',
            'class' : "form-control w-3/4 p-2 rounded-xl",
        })
    )