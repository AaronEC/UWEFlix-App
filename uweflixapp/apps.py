"""Contains only the basic Django configuration for the app"""

from django.apps import AppConfig


class UweflixappConfig(AppConfig):
    """Basic Django configuration for the app"""
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'uweflixapp'
