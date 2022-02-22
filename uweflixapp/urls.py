from django.urls import path
from .views import Home

app_name = 'uweflixapp'

urlpatterns = [
    path('', Home, name="home")
    ]
