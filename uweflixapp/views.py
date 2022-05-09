from urllib import request
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Movie, Showing
from django.views.generic import CreateView
from .forms import RegisterForm

class Home(View):
    def get(self, request, *args, **kwargs):
        # Redirect to profile page if logged in
        if request.user.is_authenticated:
            return redirect('uweflixapp:movie-list')
        return render(request, 'index.html')
    
method_decorator(login_required, name='dispatch')
class MovieList(View):
    
    def get(self, request, *args, **kwargs):

            movies = Movie.objects.filter()
            
            context = {
                'movies':movies
            }   

            return render(request, 'movielist.html', context)

        
method_decorator(login_required, name='dispatch')
class MovieDetail(View):
    
    def get(self, request, movie_id, *args, **kwargs):
        try:
            movie = Movie.objects.get(uuid=movie_id)
            showings = Showing.objects.filter(movie=movie)

            context = {
                'movie':movie,
                'showings':showings
            }   
            
            return render(request, 'moviedetail.html', context)
        except Movie.DoesNotExist:
            return redirect('uweflixapp:profile-list')
        
method_decorator(login_required, name='dispatch')
class SeatList(View):
    def get(self, request, showing_id, *args, **kwargs):
        
        showing = Showing.objects.get(uuid=showing_id)
        
        seats = showing.seats
        tally = ""
        screen = showing.screen
        price = showing.price
        discount = request.user.discount
        social_distance = showing.COVID_toggle
        
        if request.user.is_staff:
            price = f"{price - (price * (discount / 100))} ({discount}% Club dicount applied!)"
        
        for x in range(seats):
            tally = tally + "1"
        if social_distance:
            tally= tally[:len(tally)//2]
            print(tally)
                
        context = {
            'seats':tally,
            'screen':screen,
            'price':price,
            'social_distance':social_distance
        }
        return render(request, 'seatlist.html', context)
        
class RegisterView(CreateView):
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'