from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class UserRegistrationForm(UserCreationForm):
    email = forms.EmailField()
    firstname = forms.CharField(label='First Name', max_length=30)
    lastname = forms.CharField(label='Last Name', max_length=150)

    class Meta:
        model=User
        fields=['username', 'firstname', 'lastname', 'email', 'password1', 'password2']
