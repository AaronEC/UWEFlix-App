from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .forms import ProfileForm
from .models import Profile

class Home(View):
    def get(self, request, *args, **kwargs):
        
        # Redirect to profile page if logged in
        if request.user.is_authenticated:
            return redirect('uweflixapp:profile-list')
        
        return render(request, 'index.html')
    

method_decorator(login_required, name='dispatch')
class ProfileList(View):
    
    def get(self, request, *args, **kwargs):
        
        profiles = request.user.profiles.all()
        
        context = {
            'profiles':profiles
        }
        
        return render(request, 'profilelist.html', context)
    

method_decorator(login_required, name='dispatch')
class ProfileCreate(View):
    
    def get(self, request, *args, **kwargs):
        
        form = ProfileForm()
        
        context = {
            'form':form
        }
        
        return render(request, 'profilecreate.html', context)
    
    def post(self, request, *args, **kwargs):
        
        form = ProfileForm(request.POST or None)
        
        if form.is_valid():
            profile = Profile.objects.create(**form.cleaned_data)
            if profile:
                request.user.profiles.add(profile)
                return redirect('uweflixapp:profile-list')
        
        context = {
            'form':form
        }
        
        return render(request, 'profilecreate.html', context)