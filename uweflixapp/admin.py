from django.contrib import admin
from uweflixapp.models import Movie, CustomUser, Showing

admin.site.register(Movie)
admin.site.register(CustomUser)
admin.site.register(Showing)