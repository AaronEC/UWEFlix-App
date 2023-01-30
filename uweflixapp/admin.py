"""Contains the admin and custom admin user models"""

from django.contrib import admin
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin

from uweflixapp.models import Movie, CustomUser, Showing

from .forms import UserAdminCreationForm, UserAdminChangeForm

User = get_user_model()

class UserAdmin(BaseUserAdmin):
    """Base user admin"""
    # The forms to add and change user instances
    form = UserAdminChangeForm
    add_form = UserAdminCreationForm

    # The fields to be used in displaying the User model.
    # These override the definitions on the base UserAdmin
    # that reference specific fields on auth.User.
    list_display = ['email', 'admin', 'club_rep', 'cinema_manager', 'account_manager']
    list_filter = ['active', 'admin', 'club_rep', 'cinema_manager', 'account_manager']
    fieldsets = (
        (None, {'fields': ('email', 'password', 'discount')}),
        ('Permissions', {'fields': ('active', 'staff', 'admin',
                        'club_rep', 'cinema_manager', 'account_manager')}),
    )
    # add_fieldsets is not a standard ModelAdmin attribute. UserAdmin
    # overrides get_fieldsets to use this attribute when creating a user.
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2')}
        ),
    )
    search_fields = ['email']
    ordering = ['email']
    filter_horizontal = ()

class CustomUserAdmin(UserAdmin):
    """Custom admin for super user"""

    def get_form(self, request, obj=None, **kwargs):
        """Admin form view"""

        form = super().get_form(request, obj, **kwargs)

        return form

    def has_delete_permission(self, request, obj=None):
        return True if request.user.is_admin else True if request.user.is_amanager else False

    def has_add_permission(self, request, obj=None):
        return True if request.user.is_admin else True if request.user.is_amanager else False

    def has_change_permission(self, request, obj=None):
        return True if request.user.is_admin else True if request.user.is_amanager else False

# Remove Group Model from admin. We're not using it.
admin.site.unregister(Group)
admin.site.register(Movie)
admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Showing)
