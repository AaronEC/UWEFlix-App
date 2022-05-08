from email.mime import image
from operator import truediv
from pyexpat import model
from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractUser
import uuid

# Categorisation tuples, format (backend, frontent)
USER_TYPE = (
    ('account_manager', 'Account Manager'),
    ('club_rep', 'Club Rep'),
    ('student', 'Student')
)
MOVIE_CHOICES = (
    ('seasonal', 'Seasonal'),
    ('single', 'Single')
)

class CustomUser(AbstractUser):
    name = models.CharField(max_length=1000, blank=True)
    user_type = models.CharField(choices=USER_TYPE, max_length=15, null=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    
    def __str__(self) -> str:
        return self.title
    
class Movie(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    created = models.DateTimeField(auto_now_add=True)
    uuid = models.UUIDField(default=uuid.uuid4)
    # type = models.CharField(choices=MOVIE_CHOICES, max_length=10, null=True)
    banner = models.ImageField(upload_to='covers')
    poster = models.ImageField(upload_to='posters')
    trailer_link = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.title
    
class Showing(models.Model):
    name = models.CharField(max_length=1000)
    date = models.DateTimeField()
    screen = models.IntegerField()
    movie = models.ManyToManyField('Movie')
    price = models.IntegerField()
    
    def __str__(self) -> str:
        return f"{self.name} - Screen {self.screen} {self.date}."