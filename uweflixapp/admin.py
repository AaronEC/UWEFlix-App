from django.contrib import admin

# Register your models here.
from .models import *
admin.site.register(Customer)
admin.site.register(Film)
admin.site.register(Showing)
admin.site.register(UniversityClub)
admin.site.register(ClubRepresentative)
admin.site.register(Screen)
admin.site.register(Account)
admin.site.register(Booking)
