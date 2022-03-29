from http.client import ImproperConnectionState
from django.db import IntegrityError
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.db import IntegrityError

def Home(request):
    return render(request, 'index.html')

def signnewuser(request):
    if request.method=="POST":
        if request.POST.get('password1') == request.POST.get('password2'):
            try:
                saveuser=User.objects.create_user(request.POST.get('username'), password=request.POST.get('password1'))
                saveuser.save()
                return render(request, 'signup.html', {'form': UserCreationForm(), 'info': 'The User '+request.POST.get('username')+' is saved successfully'})
            except IntegrityError:
                return render(request, 'signup.html', {'form': UserCreationForm(), 'info': 'The User '+request.POST.get('username')+' already exists..'})
        else:
            return render(request, 'signup.html', {'form': UserCreationForm(), 'error': 'The passwords are not matching'})

    else:
        return render(request, 'signup.html', {'form': UserCreationForm})


def loginuser(request):
    if request.method=="POST":
        loginsuccess=authenticate(request,username=request.POST.get('username'), password=request.POST.get('password'))
        if loginsuccess is None:
            return render(request, 'login.html', {'form': AuthenticationForm(), 'error': 'The username & password are wrong'})
        else:
            login(request,loginsuccess)
            return redirect('welcomepage')
    else:
        return render(request, 'login.html', {'form': AuthenticationForm()})

def logoutpage(request):
    if request.method=="POST":
        logout(request)
        return redirect('loginuser')