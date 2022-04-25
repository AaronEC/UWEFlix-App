from dataclasses import field
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms

from uweflixapp import models
from .models import Film, Showing, UniversityClub, ClubRepresentative, Account, Screen


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

class ClubForm(ModelForm):
    class Meta:
        model = UniversityClub
        fields = '__all__'

class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = '__all__'

class ShowingForm(ModelForm):
    class Meta:
        model = Showing
        fields = '__all__'

class ClubRepresentativeForm(ModelForm):
    class Meta:
        model = ClubRepresentative
        fields = '__all__'

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']