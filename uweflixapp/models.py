"""Contains models for:
- UserManager
- CustomUser
- Profile (optional additional user information *NYI)
- Movie
- Showing
"""

import uuid

from django.contrib.auth.models import AbstractBaseUser, BaseUserManager
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db import models


class UserManager(BaseUserManager):
    """User manager for basic functions, more authentication is provided by allauth,
    see settings.py
    """

    def create_user(self, email, password=None, is_active=True, is_staff=False, is_admin=False):
        """Checks email and pass, sets account level."""

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
        """Club rep user, for club discounts."""

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
    """Custom user model based off Django default.

    Uses Abstract User as we want to identify using email address.

    Uses AbstractBaseUser to define our own, more relevant data fields.
    """
    email        = models.EmailField(max_length=255, unique=True)
    active       = models.BooleanField(default=True)  # Account enabled
    staff        = models.BooleanField(default=False)
    admin        = models.BooleanField(default=False) # superuser
    club_rep     = models.BooleanField(default=False)
    cinema_manager  = models.BooleanField(default=False)
    account_manager = models.BooleanField(default=False)
    discount     = models.IntegerField(
        default=0,
        validators=[
            MaxValueValidator(100),
            MinValueValidator(0)
        ]
     )

    USERNAME_FIELD = 'email'
    REQUIRED_FILEDS = []    # Not used now maybe later for validation.

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

    def has_perm(self):
        "Does the user have a specific model level permission?"
        return True

    def has_module_perms(self):
        "Does the user have permissions to view the app?"
        return True

    def has_delete_permission(self):
        "Does the user have permissions to delete objects?"
        return False

    def __str__(self) -> str:
        return self.email


class Profile(models.Model):
    """This may be used later to add additional user information without
    changing the CustomUser model."""
    # user = models.OneToOneField(CustomUser)
    # Extra data goes here

    
class Movie(models.Model):
    """Data model for individual movies"""

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
    """Data model for individual showings"""

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
    uuid         = models.UUIDField(default=uuid.uuid4)
    COVID_toggle = models.BooleanField(default=False)

    def __str__(self) -> str:
        return f"{self.movie} - Screen {self.screen} {self.date}."
