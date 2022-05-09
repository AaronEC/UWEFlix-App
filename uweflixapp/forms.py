from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Booking, Film, Showing, UniversityClub, ClubRepresentative, Account, Screen, User, Cost



class CustomRepCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name", "rep_id", "address")

class CustomStudentCreationForm(UserCreationForm):
    class Meta:
        model = User
        fields = ("username", "email", "first_name", "last_name")


class FilmForm(ModelForm):
    class Meta:
        model = Film
        fields = '__all__'

class ClubForm(ModelForm):
    class Meta:
        model = UniversityClub
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(ClubForm, self).__init__(*args, **kwargs)
        self.fields['club_rep'].queryset = User.objects.filter(is_rep=True)# or something else

class ScreenForm(forms.ModelForm):
    class Meta:
        model = Screen
        fields = '__all__'

class ShowingForm(ModelForm):
    class Meta:
        model = Showing
        fields = '__all__'
        widgets = {'available_seats': forms.HiddenInput()}

class ClubRepresentativeForm(ModelForm):
    class Meta:
        model = ClubRepresentative
        fields = '__all__'

class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = '__all__'


class BookingForm(forms.ModelForm):
    class Meta:
        model = Booking
        fields = '__all__'


class CostForm(forms.ModelForm):
    class Meta:
        model = Cost
        fields = '__all__'