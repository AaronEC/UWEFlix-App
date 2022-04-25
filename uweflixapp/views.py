import imp
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

from django.contrib.auth.decorators import login_required

# Create your views here.
from .models import *
from .forms import ClubForm, ShowingForm, FilmForm, CreateUserForm
from .filters import FilmFilter

# registers users
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)

            if form.is_valid():
                user = form.save()
                user.is_active = False
                user.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Acount was created for ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'uweflixapp/register.html', context)

# logs in users
def loginPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password =request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                return redirect('home')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'uweflixapp/login.html', context)

# logs out user
def logoutUser(request):
    logout(request)
    return redirect('login')

# returns home url
def home(request):

    return render(request, 'uweflixapp/clubs.html')

# adds film
def addFilm(request):
    form = FilmForm()
    if request.method == 'POST':
        form = FilmForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('films')

    context = {'form':form}
    return render(request, 'uweflixapp/film_form.html', context)

# adds showing
def addShowing(request):
    form = ShowingForm()
    if request.method == 'POST':
        form = ShowingForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('showings')

    context = {'form':form}
    return render(request, 'uweflixapp/showing_form.html', context)

# adds club
def addClub(request):
    form = ClubForm()
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clubs')

    context = {'form':form}
    return render(request, 'uweflixapp/club_form.html', context)

# returns films
def films(request):
    films = Film.objects.all()
    return render(request, 'uweflixapp/films.html', {'films': films})

# returns users not approved yet
def customer(request):
    customer = Customer.objects.all()
    return render(request, 'uweflixapp/customer.html', {'customer': customer})

# # returns showings
def showings(request):
    showings = Showing.objects.all()
    return render(request, 'uweflixapp/showings.html', {'showings': showings})

# returns university clubs
def clubs(request):
    clubs = UniversityClub.objects.all()
    return render(request, 'uweflixapp/clubs.html', {'clubs': clubs})

# returns future showings
def viewShowings(request):
    films = Film.objects.all()
    return render(request, 'uweflixapp/booking.html', {'films': films})

# selects showing and returns details of showing
def selectShowing(request):

    return


# deletes film
def deletesFilm(request, pk):
    film = Film.objects.get(id=pk)

    if request.method == "POST":
        film.delete()
        return redirect('/')

    context = {'film':film}
    return render(request, 'uweflixapp/delete.html', context)


