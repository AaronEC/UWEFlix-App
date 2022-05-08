from django.forms import ModelForm
from uweflixapp.models import Profile

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        exclude = ['uuid']