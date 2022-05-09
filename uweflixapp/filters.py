from django.forms import DateInput
import django_filters
from .models import *

class ShowFilter(django_filters.FilterSet):
    date = django_filters.DateFilter(widget=DateInput(attrs={'type': 'date'}))

    class Meta:
        model = Showing
        fields = ['date']

class BookingFilter(django_filters.FilterSet):
    class Meta:
        model = Booking
        fields = '__all__'