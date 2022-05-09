from django.contrib import admin
from django.contrib.auth.admin import UserAdmin




# Register your models here.
from .models import *

admin.site.register(User)
admin.site.register(Film)
admin.site.register(Distancing)
admin.site.register(Cost)
admin.site.register(Showing)
admin.site.register(UniversityClub)
admin.site.register(ClubRepresentative)
admin.site.register(Screen)
admin.site.register(Account) 
admin.site.register(Booking)
