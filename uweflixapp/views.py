from urllib import request
from django.shortcuts import redirect, render
from django.views import View
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from .models import Movie, Showing

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
            