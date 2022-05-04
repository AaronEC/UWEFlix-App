from pyexpat import model
from django.contrib.auth.models import PermissionsMixin, AbstractBaseUser, BaseUserManager
from tkinter import CASCADE
from unicodedata import name
from django.db import models



class User_manager(BaseUserManager):
    def create_user(self, username, email, first_name, last_name, user_type, password):
        email = self.normalize_email(email)
        user = self.model(username=username, email=email, first_name=first_name, last_name=last_name, user_type=user_type)
        user.set_password(password)
        user.save(using=self.db)
        return user

    def create_superuser(self, username, email, password, first_name=None, last_name=None, user_type=None):
        user = self.create_user(username=username, email=email, first_name=first_name, last_name=last_name, user_type=user_type, password=password)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        return user

class User(PermissionsMixin, AbstractBaseUser):
    username = models.CharField(max_length=32, unique=True, )
    email = models.EmailField(max_length=32)
    first_name = models.CharField(max_length=32, blank=True, null=True)
    last_name = models.CharField(max_length=32, blank=True, null=True)
    user_type_choices = [("Student", "Student"), ("Representative", "Representative")]
    user_type = models.CharField(choices=user_type_choices, default="Student", max_length=14)

    is_active = models.BooleanField(default=False)
    is_staff = models.BooleanField(default=False)
    REQUIRED_FIELDS = ["email", "first_name", "last_name", "user_type"]
    USERNAME_FIELD = "username"
    objects = User_manager()

    def __str__(self):
        return self.username
        

class ClubRepresentative(models.Model):
    club_rep_id = models.CharField(max_length=6, null=True, unique=True)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=8, null=True, unique=True)

    def generate_id():
        return


class UniversityClub(models.Model):
    club_name = models.CharField(max_length=200, null=True, blank=False)
    street_number = models.IntegerField(null=True)
    street = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)
    telephone = models.IntegerField(null=True)
    mobile = models.IntegerField(null=True)
    email = models.CharField(max_length=200, null=True)
    club_rep = models.ForeignKey(ClubRepresentative, null=True, on_delete=models.SET_NULL)
    debit_amount = models.IntegerField(null=True, default=0)

    def __str__(self):
        return self.club_name


class Film(models.Model):
    AGE_RATINGS  = (
        ('12+', '12+'),
        ('15+', '15+'),
        ('18+', '18+'),
        ('PG-13', 'PG-13')
    )
    
    title = models.CharField(max_length=50, null=True, blank=False)
    age_rating = models.CharField(blank=False, null=False, max_length=7, choices=AGE_RATINGS, default='string')
    duration = models.IntegerField(null=True, blank=False)
    description = models.CharField(max_length=250, null=True, blank=False)
    

    def __str__(self):
        return self.title

class Screen(models.Model):
    screen_id = models.CharField(max_length=50, null=False, blank=False)
    seats = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.screen_id


class Showing(models.Model):
    film = models.ForeignKey(Film, null=True, on_delete=models.CASCADE, blank=False)
    date = models.DateField(null=True, blank=False)
    time = models.TimeField(null=True, blank=False)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, null=False, blank=False)
    
    def __str__(self):
        return self.film.title

class Account(models.Model):
    club = models.ForeignKey(UniversityClub, on_delete=models.CASCADE, null=False, blank=False)
    title = models.CharField(max_length=50, null=False, blank=False)
    card_number = models.IntegerField(null=False, blank=False)
    expiry_date = models.IntegerField(null=False, blank=False)

    def __str__(self):
        return self.club

class Booking(models.Model):
    #adult_ticket = models.IntegerField(default=0, blank=False, null=True)
    #child_ticket = models.IntegerField(default=0, blank=False, null=True)
    #student_ticket = models.IntegerField(default=0, blank=False, null=True)
    ticket_quantity = models.IntegerField(default=0, blank=False, null=True)
    total_cost = models.IntegerField(null=False, blank=False)
    customer = models.ForeignKey(User, on_delete=models.CASCADE, null=False)
    date_created = models.DateTimeField(auto_now_add=True, null=True)
