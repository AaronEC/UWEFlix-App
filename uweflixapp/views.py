import datetime
import imp
from itertools import count
from unittest.util import _MAX_LENGTH
from urllib import request
from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import BookingForm, CustomUserCreationForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
from .models import *
from .forms import ScreenForm, ClubForm, ShowingForm, FilmForm
from .filters import ShowFilter


# PERMISSIONS
def must_be_cinema_manager(user):
    return user.groups.filter(name='Cinema Manager').count()

#@user_passes_test(must_be_cinema_manager)

# registers users
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CustomUserCreationForm()
        if request.method == 'POST':
            form = CustomUserCreationForm(request.POST)

            if form.is_valid():
                user = form.save()
                user.is_active = False
                user.save()
                if user.user_type == "Student":
                    g = Group.objects.get(name='Student')
                    g.user_set.add(user)
                elif user.user_type == "Student":
                    g = Group.objects.get(name='Representative')
                    g.user_set.add(user)
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
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)
            
            if user is not None:
                login(request, user)
                if user.is_superuser:
                    return redirect('clubs')
                else:
                    return redirect('view_showings')
            else:
                messages.info(request, 'Username OR password is incorrect')

        context = {}
        return render(request, 'uweflixapp/login.html', context)

# logs out user
def logoutUser(request):
    logout(request)
    return redirect('login')

# returns home url
@user_passes_test(must_be_cinema_manager)
def home(request):

    return render(request, 'uweflixapp/clubs.html')

# adds film
@user_passes_test(must_be_cinema_manager)
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
@user_passes_test(must_be_cinema_manager)
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
@user_passes_test(must_be_cinema_manager)
def addClub(request):
    form = ClubForm()
    if request.method == 'POST':
        form = ClubForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('clubs')

    context = {'form':form}
    return render(request, 'uweflixapp/club_form.html', context)

# adds screen
@user_passes_test(must_be_cinema_manager)
def addScreen(request):
    form = ScreenForm()
    if request.method == 'POST':
        form = ScreenForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('screens')

    context = {'form':form}
    return render(request, 'uweflixapp/screen_form.html', context)

# returns films
@user_passes_test(must_be_cinema_manager)
def films(request):
    films = Film.objects.all()
    return render(request, 'uweflixapp/films.html', {'films': films})

# returns screens
@user_passes_test(must_be_cinema_manager)
def screens(request):
    screens = Screen.objects.all()
    return render(request, 'uweflixapp/screens.html', {'screens': screens})

# returns users not approved yet
@user_passes_test(must_be_cinema_manager)
def customer(request):
    user = get_user_model()
    customer = user.objects.filter(is_active__in=[False])
    return render(request, 'uweflixapp/customer.html', {'customer': customer})

# # returns showings
@user_passes_test(must_be_cinema_manager)
def showings(request):
    showings = Showing.objects.all()
    return render(request, 'uweflixapp/showings.html', {'showings': showings})

# returns university clubs
@user_passes_test(must_be_cinema_manager)
def clubs(request):
    clubs = UniversityClub.objects.all()
    return render(request, 'uweflixapp/clubs.html', {'clubs': clubs})

# modify film
@user_passes_test(must_be_cinema_manager)
def modifyFilm(request, pk):
    film = Film.objects.get(id=pk)
    form = FilmForm(instance=film)

    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = FilmForm(request.POST, instance=film)
        if form.is_valid():
            form.save()
            return redirect('films')

    context = {'form':form}
    return render(request, 'uweflixapp/film_form.html', context)

# modify Showing
@user_passes_test(must_be_cinema_manager)
def modifyShowing(request, pk):
    showing = Showing.objects.get(id=pk)
    form = ShowingForm(instance=showing)

    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = ShowingForm(request.POST, instance=showing)
        if form.is_valid():
            form.save()
            return redirect('showings')

    context = {'form':form}
    return render(request, 'uweflixapp/showing_form.html', context)

# modify Screen
@user_passes_test(must_be_cinema_manager)
def modifyScreen(request, pk):
    screen = Screen.objects.get(id=pk)
    form = ScreenForm(instance=screen)

    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = ScreenForm(request.POST, instance=screen)
        if form.is_valid():
            form.save()
            return redirect('Screens')

    context = {'form':form}
    return render(request, 'uweflixapp/screen_form.html', context)

# deletes film
@user_passes_test(must_be_cinema_manager)
def deletesFilm(request, pk):
    film = Film.objects.get(id=pk)

    if request.method == "POST":
        film.delete()
        return redirect('films')

    context = {'film':film}
    return render(request, 'uweflixapp/delete_film.html', context)

# deletes Screen
@user_passes_test(must_be_cinema_manager)
def deletesScreen(request, pk):
    screen = Screen.objects.get(id=pk)

    if request.method == "POST":
        screen.delete()
        return redirect('screens')

    context = {'screen':screen}
    return render(request, 'uweflixapp/delete_screen.html', context)

# deletes Showing
@user_passes_test(must_be_cinema_manager)
def deletesShowing(request, pk):
    showing = Showing.objects.get(id=pk)

    if request.method == "POST":
        showing.delete()
        return redirect('showings')

    context = {'showing':showing}
    return render(request, 'uweflixapp/delete_showing.html', context)

# approve user
@user_passes_test(must_be_cinema_manager)
def approveUser(request, pk): 
    user = get_user_model()
    customer = user.objects.get(id=pk)
    
    if request.method == "POST":
        customer.is_active = True
        #password = User.objects.make_random_password(length=8)
        #customer.set_password('password123')
        customer.save()
        return redirect('customer')

    context = {'customer':customer}
    return render(request, 'uweflixapp/approve.html', context)

# deny user
@user_passes_test(must_be_cinema_manager)
def denyUser(request, pk): 
    user = get_user_model()
    customer = user.objects.get(id=pk)
    
    if request.method == "POST":
        customer.delete()
        return redirect('customer')

    context = {'customer':customer}
    return render(request, 'uweflixapp/deny.html', context)


# returns future showings
def viewShowings(request):
    showings = Showing.objects.all()

    myFilter = ShowFilter(request.GET, queryset=showings)
    showings = myFilter.qs

    context = {'showings':showings, 'myFilter':myFilter}
    return render(request, 'uweflixapp/view_showings.html', context)


# selects showing and returns details of showing
def selectShowing(request, pk):
    showing = Showing.objects.get(id=pk)

    film = showing.film
    duration = showing.film.duration
    age_rating = showing.film.age_rating
    description = showing.film.description
    date = showing.date
    time = showing.time
    screen = showing.screen

    context = {'showing': showing, 'film':film, 'duration':duration, 'age_rating':age_rating, 'description':description, 'date':date, 'time':time, 'screen':screen}
    return render(request, 'uweflixapp/showing_details.html', context)


# create booking
def createBooking(request):
    TICKET_COST = 7.0

    booking = Booking()
    ticket_quantity = booking.objects.ticket_quantity()
    

    context = {'ticket_quantity':ticket_quantity}
    return render(request, 'uweflixapp/booking_successful.html', context)



def placeOrder(request):
    #and newbooking.is_valid()
    if request.method == "POST":
        newbooking = BookingForm()
        if newbooking.is_valid():
            newbooking.customer = request.user
            newbooking.ticket_quantity = request.POST.get('ticket_quantity')
            newbooking.total_cost = request.POST.get('total_cost')
            newbooking.save()

    context = {}

    #messages.success(request, "Your order has been placed successfully")

    return redirect('view_showings')

# cancel Booking
def cancelBooking():
    return

# returns transactions from past 30 days
@user_passes_test(must_be_cinema_manager)
def viewTransactions(request):
    last_30_days = datetime.datetime.today() - datetime.timedelta(30)
    transactions = Booking.objects.filter(date_created__gte=last_30_days)

    context = {'transactions':transactions}
    return render(request, 'uweflixapp/transactions.html', context)

# toggle social distancing
def toggledistancing():
    return


