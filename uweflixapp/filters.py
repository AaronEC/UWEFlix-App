from csv import excel
import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class FilmFilter(django_filters.FilterSet):


    class Meta:
        model = Film
        fields = '__all__'
