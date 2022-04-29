from csv import excel
import django_filters
from django_filters import DateFilter, CharFilter

from .models import *

class ShowFilter(django_filters.FilterSet):
    class Meta:
        model = Showing
        fields = '__all__'
        exclude = ['film', 'time', 'screen']
