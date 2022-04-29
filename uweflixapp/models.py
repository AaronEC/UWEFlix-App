from tkinter import CASCADE
from unicodedata import name
from django.db import models

""" class User(AbstractUser):
      CINEMA_MANAGER = 1
      ACCOUNT_MANAGER = 2
      CLUB_REPRESENTATIVE = 3
      STUDENT = 4

      ROLE_CHOICES = (
          (CINEMA_MANAGER, 'Cinema Manager'),
          (ACCOUNT_MANAGER, 'Account Manager'),
          (CLUB_REPRESENTATIVE, 'Club Representative'),
          (STUDENT, 'Student'),
      )
      role = models.PositiveSmallIntegerField(choices=ROLE_CHOICES, blank=True, null=True) """

# Create your models here.
class Customer(models.Model):
    name = models.CharField(max_length=50, null=True)
    phone = models.CharField(max_length=11, null=True)
    email = models.CharField(max_length=50, null=True)
    date_created = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.name


class UniversityClub(models.Model):
    auto_increment_club_id = models.AutoField(primary_key=True)
    club_name = models.CharField(max_length=200, null=True)
    street_number = models.IntegerField(null=True)
    street = models.CharField(max_length=200, null=True)
    city = models.CharField(max_length=200, null=True)
    postcode = models.CharField(max_length=200, null=True)
    telephone = models.IntegerField(null=True)
    mobile = models.IntegerField(null=True)
    email = models.CharField(max_length=200, null=True)
    club_rep = models.ForeignKey(Customer, null=True, on_delete=models.SET_NULL)
    debit_amount = models.IntegerField(null=True)

    def __str__(self):
        return self.club_name

class ClubRepresentative(models.Model):
    club = models.ForeignKey(UniversityClub, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50, null=False, blank=False)
    last_name = models.CharField(max_length=50, null=False, blank=False)
    date_of_birth = models.DateField()
    password = models.CharField(max_length=8, null=True, unique=True)
    club_rep_id = models.CharField(max_length=6, null=True, unique=True)

class Film(models.Model):
    AGE_RATINGS  = (
        ('12+', '12+'),
        ('15+', '15+'),
        ('18+', '18+'),
        ('PG-13', 'PG-13')
    )
    
    title = models.CharField(max_length=50, null=True)
    age_rating = models.CharField(blank=False, null=False, max_length=7, choices=AGE_RATINGS, default='string')
    duration = models.IntegerField(null=True)
    description = models.CharField(max_length=250, null=True, blank=True)
    

    def __str__(self):
        return self.title

class Screen(models.Model):
    screen_id = models.CharField(max_length=50, null=False, blank=False)
    seats = models.IntegerField(null=False)

    def __str__(self):
        return self.screen_id


class Showing(models.Model):
    auto_increment_id = models.AutoField(primary_key=True)
    film = models.ForeignKey(Film, null=True, on_delete=models.SET_NULL)
    date = models.DateField(null=True)
    time = models.TimeField(null=True)
    screen = models.ForeignKey(Screen, on_delete=models.CASCADE, null=False)

    def __str__(self):
        return self.film.title

class Account(models.Model):
    club = models.ForeignKey(UniversityClub, on_delete=models.CASCADE, null=False)
    title = models.CharField(max_length=50, null=False)
    card_number = models.IntegerField(null=False)
    expiry_date = models.IntegerField(null=False)

    def __str__(self):
        return self.club


class Booking(models.Model):
    """ TICKET_TYPE  = (
        ('Child', 'Child'),
        ('Adult', 'Adult'),
        ('Student', 'Student'),
    )
 """
    auto_increment_id = models.AutoField(primary_key=True)
    ticket_quantity = models.IntegerField(null=False)
    #ticketType = models.CharField(blank=False, null=False, max_length=7, choices=TICKET_TYPE, default='string')
    adult_ticket = models.IntegerField()
    child_ticket = models.IntegerField()
    student_ticket = models.IntegerField()
    total_cost = models.IntegerField(null=False)
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE, null=False)
    showing = models.ForeignKey(Showing, on_delete=models.CASCADE, null=False)




