import datetime
from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib.auth.models import Group
from django.contrib.auth.decorators import login_required
from .forms import CustomRepCreationForm, CustomStudentCreationForm
from django.contrib.auth.decorators import user_passes_test

# Create your views here.
from .models import *
from .forms import ScreenForm, ClubForm, ShowingForm, FilmForm
from .filters import ShowFilter

# PERMISSIONS
def must_be_cinema_manager(user):
    return user.groups.filter(name='Cinema Manager').count()

#@user_passes_test(must_be_cinema_manager)

def registerChoice(request):
    return render(request, 'uweflixapp/register_choice.html')

# registers users
def registerPage(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CustomStudentCreationForm()
        if request.method == 'POST':
            form = CustomStudentCreationForm(request.POST)

            if form.is_valid():
                user = form.save()
                user.is_active = False
                user.is_student = True
                user.save()
                if user.is_student == True:
                    g = Group.objects.get(name='Student')
                    g.user_set.add(user)
                elif user.is_rep == True:
                    g = Group.objects.get(name='Representative')
                    g.user_set.add(user)
                user = form.cleaned_data.get('username')
                messages.success(request, 'Acount was created for ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'uweflixapp/register.html', context)

# registers users
def registerPageRep(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        form = CustomRepCreationForm()
        if request.method == 'POST':
            form = CustomRepCreationForm(request.POST)

            if form.is_valid():
                user = form.save()
                user.is_rep = True
                user.is_active = False
                user.save()
                if user.is_student == True:
                    g = Group.objects.get(name='Student')
                    g.user_set.add(user)
                elif user.is_rep == True:
                    g = Group.objects.get(name='Representative')
                    g.user_set.add(user)
                user = form.cleaned_data.get('username')
                messages.success(request, 'Acount was created for ' + user)

                return redirect('login')

        context = {'form':form}
        return render(request, 'uweflixapp/register_rep.html', context)

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
            showing = Showing.objects.last()
            showing.available_seats = showing.screen.seats
            showing.save()

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

# adds screen
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
def films(request):
    films = Film.objects.all()
    return render(request, 'uweflixapp/films.html', {'films': films})

# returns films
def costs(request):
    costs = Cost.objects.all()
    return render(request, 'uweflixapp/costss.html', {'costs': costs})

# returns screens
def screens(request):
    screens = Screen.objects.all()
    return render(request, 'uweflixapp/screens.html', {'screens': screens})

# returns users not approved yet
def customer(request):
    user = get_user_model()
    customer = user.objects.filter(is_active__in=[False])
    return render(request, 'uweflixapp/customer.html', {'customer': customer})

# # returns showings
def showings(request):
    showings = Showing.objects.all()
    return render(request, 'uweflixapp/showings.html', {'showings': showings})

# returns university clubs
def clubs(request):
    clubs = UniversityClub.objects.all()
    return render(request, 'uweflixapp/clubs.html', {'clubs': clubs})

# modify film
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
def modifyScreen(request, pk):
    screen = Screen.objects.get(id=pk)
    form = ScreenForm(instance=screen)

    if request.method == 'POST':
        #print('Printing POST:', request.POST)
        form = ScreenForm(request.POST, instance=screen)
        if form.is_valid():
            form.save()
            return redirect('screens')

    context = {'form':form}
    return render(request, 'uweflixapp/screen_form.html', context)

# deletes film
def deletesFilm(request, pk):
    film = Film.objects.get(id=pk)

    if request.method == "POST":
        film.delete()
        return redirect('films')

    context = {'film':film}
    return render(request, 'uweflixapp/delete_film.html', context)

# deletes Screen
def deletesScreen(request, pk):
    screen = Screen.objects.get(id=pk)

    if request.method == "POST":
        screen.delete()
        return redirect('screens')

    context = {'screen':screen}
    return render(request, 'uweflixapp/delete_screen.html', context)

# deletes Showing
def deletesShowing(request, pk):
    showing = Showing.objects.get(id=pk)

    if request.method == "POST":
        showing.delete()
        return redirect('showings')

    context = {'showing':showing}
    return render(request, 'uweflixapp/delete_showing.html', context)

# approve user
def approveUser(request, pk): 
    user = get_user_model()
    # set selected user
    customer = user.objects.get(id=pk)
    
    if request.method == "POST":
        # toggle user to is_active = True
        customer.is_active = True
        #password = User.objects.make_random_password(length=8)
        #customer.set_password('password123')
        customer.save()
        return redirect('customer')

    context = {'customer':customer}
    return render(request, 'uweflixapp/approve.html', context)

# deny user
def denyUser(request, pk): 
    user = get_user_model()
    # set selected user
    customer = user.objects.get(id=pk)
    
    if request.method == "POST":
        # delete user
        customer.delete()
        return redirect('customer')

    context = {'customer':customer}
    return render(request, 'uweflixapp/deny.html', context)

# returns future showings
def viewShowings(request):
    today = datetime.datetime.today()
    # filter future showing 
    showings = Showing.objects.filter(date__gte=today)

    myFilter = ShowFilter(request.GET, queryset=showings)
    showings = myFilter.qs

    context = {'showings':showings, 'myFilter':myFilter}
    return render(request, 'uweflixapp/view_showings.html', context)

# selects showing and returns details of showing
def selectShowing(request, pk):
    # set showing to instance of selected shwoing
    showing = Showing.objects.get(id=pk)
    # assign local variables to fields of instance
    film = showing.film
    duration = showing.film.duration
    age_rating = showing.film.age_rating
    description = showing.film.description
    date = showing.date
    time = showing.time
    screen = showing.screen
    seats = showing.available_seats

    context = {'showing': showing, 'film':film, 'duration':duration, 'age_rating':age_rating, 'description':description, 'date':date, 'time':time, 'screen':screen, 'seats':seats}
    return render(request, 'uweflixapp/showing_details.html', context)

# calculate total price of tickets
def calcTotalCost(adult_quantity, child_quantity, student_quantity):
    cost = Cost.objects.first()
    adult_ticket_cost = cost.adult_cost
    child_ticket_cost = cost.child_cost

    total_price = (int(adult_quantity)*float(adult_ticket_cost))+(int(child_quantity)*float(child_ticket_cost))+(int(student_quantity)*float(adult_ticket_cost))
    return total_price

    # calculate total price of tickets for student user
def calcTotalCostStudent(adult_quantity, child_quantity, student_quantity):
    cost = Cost.objects.first()
    adult_ticket_cost = cost.adult_cost
    child_ticket_cost = cost.child_cost
    student_discount = cost.student_discount
    total_student_discount = (int(student_quantity)*float(adult_ticket_cost))*float(student_discount)
    total_student_price = int(student_quantity)*float(adult_ticket_cost)-total_student_discount
    
    total_price = (int(adult_quantity)*float(adult_ticket_cost))+(int(child_quantity)*float(child_ticket_cost))+float(total_student_price)
    return total_price

# calculate total ticket quantity
def calcTotalQuantity(adult_quantity, child_quantity, student_quantity):
    total_quantity = int(adult_quantity)+int(child_quantity)+int(student_quantity)
    return total_quantity

# view active users
def viewCustomers(request):
    user = get_user_model()
    # filter users with active accounts
    customer = user.objects.filter(is_active__in=[True])
    return render(request, 'uweflixapp/user_transactions.html', {'customer': customer})

# shows transactions for user accounts
def viewAccount(request, pk):
    user = get_user_model()
    # get selected user
    customer = user.objects.get(id=pk)

    # calculate last 30 days 
    last_30_days = datetime.datetime.today() - datetime.timedelta(30)
    # set bookings to all bookings of selected customer
    bookings = customer.booking_set.all()
    # filter transactions of customer from last 30 days
    myFilter = bookings.filter(date_created__gte=last_30_days)
    bookings = myFilter

    context = {'customer':customer, 'bookings':bookings, 'myFilter':myFilter}
    return render(request, 'uweflixapp/account.html', context)

def placeOrder(request, pk):
    #and newbooking.is_valid()
    cost = Cost.objects.first()
    CLUB_DISCOUNT = cost.club_discount
    if request.method == "POST":
        # creat instance
        newbooking = Booking()
        # check if user is logged in as anonymous
        if request.user.is_anonymous:
            # set user as None input to booking instance
            newbooking.customer = None
        else:
            # set user as request input to booking instance
            newbooking.customer = request.user

        # set ticket quantity inputs to booking instance
        # set empty inputs to 0
        newbooking.child_ticket = request.POST.get('child_ticket')
        if newbooking.child_ticket == '':
            newbooking.child_ticket = 0
        newbooking.adult_ticket = request.POST.get('adult_ticket')
        if newbooking.adult_ticket == '':
            newbooking.adult_ticket = 0
        newbooking.student_ticket = request.POST.get('student_ticket')
        if newbooking.student_ticket == '':
            newbooking.student_ticket = 0

        # set ticket quantity inputs
        child_ticket = request.POST.get('child_ticket')
        adult_ticket = request.POST.get('adult_ticket')
        student_ticket = request.POST.get('student_ticket')

        # validate empty tickets
        if child_ticket == '':
            child_ticket = '0'
        if adult_ticket == '':
            adult_ticket = '0'
        if student_ticket == '':
            student_ticket = '0'
        
        # check if user is representative
        if request.user.is_rep == True:
            # calculate discount price and add to booking instance
            discount = calcTotalCost(adult_ticket, child_ticket, student_ticket)*float(CLUB_DISCOUNT)
            newbooking.total_cost = calcTotalCost(adult_ticket, child_ticket, student_ticket)-discount
            # calculate total tickets
            total_quantity = calcTotalQuantity(adult_ticket, child_ticket, student_ticket)
            # if less than 10, display message
            if total_quantity < 10:
                messages.error(request,'Minimum ticket quantity for club booking is 10')
                return redirect('view_showings')
        # check if user is student
        elif request.user.is_student == True:
            # calculate discount price and add to booking instance
            #discount = calcTotalCostStudent(adult_ticket, child_ticket, student_ticket)
            newbooking.total_cost = calcTotalCostStudent(adult_ticket, child_ticket, student_ticket)#-discount
        elif request.user.is_staff:
            # calculate price and add to booking instance
            newbooking.total_cost = calcTotalCost(adult_ticket, child_ticket, student_ticket)

        # calculate total quantity
        total_quantity = calcTotalQuantity(adult_ticket, child_ticket, student_ticket)
        showing = Showing.objects.get(id=pk)
        # calculate new available seats
        available_seats = showing.available_seats
        updated_seats = available_seats-total_quantity

        # check is seats are available for booking
        if updated_seats >= 0:
            # update available seats
            Showing.objects.filter(id=pk).update(available_seats=updated_seats)
            # check if quantity is greater than 1
            if total_quantity > 0:
                # save booking instance
                newbooking.save()
                return redirect('view_showings')
        else:
            # cancel booking and redirect
            messages.error(request,'Insufficient Tickets')
            return redirect('view_showings')


# toggle social distancing
def toggledistancing(request):
    social_distancing = False
    if request.method == "POST":
        social_distancing = True
    return social_distancing
