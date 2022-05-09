import email
from email.mime import image
from lib2to3.pytree import Base
from operator import truediv
from pyexpat import model
from turtle import title
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
import uuid


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        if not email:
            raise ValueError("Email required for all users")
        if not password:
            raise ValueError("Password required for all users")
        user_obj = self.model(
            email = self.normalize_email(email)
        )
        user_obj.set_password(password)
        user_obj.active = is_active
        user_obj.rep = is_staff
        user_obj.manager = is_admin
        user_obj.save(using=self._db)
        return user_obj
    
    def create_rep_user(self, email, password=None):
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.save(using=self._db)
        return user

    
    def create_superuser(self, email, password):
        """
        Creates and saves a superuser with the given email and password.
        """
        user = self.create_user(
            email,
            password=password,
        )
        user.staff = True
        user.admin = True
        user.save(using=self._db)
        return user

class CustomUser(AbstractBaseUser):
    email        = models.EmailField(max_length=255, unique=True)
    active       = models.BooleanField(default=True) # Account enabled
    staff        = models.BooleanField(default=False)
    admin        = models.BooleanField(default=False) # superuser
    club_rep = models.BooleanField(default=False)
    cinema_manager = models.BooleanField(default=False)
    account_manager = models.BooleanField(default=False)
    discount     = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
     )
    
    USERNAME_FIELD = 'email'
    REQUIRED_FILEDS = []    # Not used now maybe later
    
    objects = UserManager()
    
    # Again not used but may be useful later #
    def get_full_name(self):
        return self.email
    
    def get_short_name(self):
        return self.email
    # Again not used but may be useful later #
    
    @property
    def is_rep(self):
        return self.club_rep
    
    @property
    def is_cmanager(self):
        return self.cinema_manager
    
    @property
    def is_amanager(self):
        return self.account_manager
    
    @property
    def is_active(self):
        return self.active
    
    @property
    def is_staff(self):
        return self.staff
    
    @property
    def is_admin(self):
        return self.admin
    
    def has_perm(self, perm, obj=None):
        "Does the user have a specific model level permission?"
        return True #if self.admin else False

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        return True #if self.admin else False
    
    def has_delete_permission(self, request, obj=None): # note the obj=None
        return False
    
    def __str__(self) -> str:
        return self.email


class Profile(models.Model):
    """This may be used later to add additional user information without 
    messing up the CustomUser model."""
    # user = models.OneToOneField(CustomUser)
    # Extra data goes here
    pass

    
class Movie(models.Model):
    title       = models.CharField(max_length=1000)
    description = models.TextField(blank=True, null=True)
    created     = models.DateTimeField(auto_now_add=True)
    uuid        = models.UUIDField(default=uuid.uuid4)
    # type      = models.CharField(choices=MOVIE_CHOICES, max_length=10, null=True)
    banner      = models.ImageField(upload_to='covers')
    poster      = models.ImageField(upload_to='posters')
    trailer_link = models.CharField(max_length=1000)
    
    def __str__(self) -> str:
        return self.title
    
class Showing(models.Model):
    date    = models.DateTimeField()
    screen  = models.PositiveIntegerField()
    movie   = models.ForeignKey('Movie', on_delete = models.CASCADE)
    price   = models.FloatField()
    seats   = models.PositiveIntegerField(
        default=50,
        validators=[
            MaxValueValidator(120),
            MinValueValidator(1)
        ]
     )
    uuid    = models.UUIDField(default=uuid.uuid4)
    COVID_toggle = models.BooleanField(default=False)
    
    def __str__(self) -> str:
        return f"{self.movie} - Screen {self.screen} {self.date}."