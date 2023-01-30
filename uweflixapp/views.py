"""Contains all the current views for the uweflix web app:
- MovieList
- MovieDetail
- SeatList
- RegisterView
"""

from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from django.utils.decorators import method_decorator
from django.views import View
from django.views.generic import CreateView

from .models import Movie, Showing
from .forms import RegisterForm


class Home(View):
    """Front page view, redirects to movie list if user is already logged in"""

    def get(self, request):
        """Renders index.html with data from DB."""
        if request.user.is_authenticated:
            return redirect('uweflixapp:movie-list')
        return render(request, 'index.html')


method_decorator(login_required, name='dispatch')
class MovieList(View):
    """View containing list of all current movies in database."""

    def get(self, request, *args, **kwargs):
        """Renders movielist.html with data from DB."""
        movies = Movie.objects.filter()
        context = {
            'movies': movies
        }

        return render(request, 'movielist.html', context)


method_decorator(login_required, name='dispatch')
class MovieDetail(View):
    """View for a specific movie with details loaded from database."""

    def get(self, request, movie_id, *args, **kwargs):
        """Renders moviedetail.html with data from DB.

        Redirects to profile* if no such movie in DB

        *Need to create error page for this.
        """
        try:
            movie = Movie.objects.get(uuid=movie_id)
            showings = Showing.objects.filter(movie=movie)
            context = {
                'movie': movie,
                'showings': showings
            }
            return render(request, 'moviedetail.html', context)

        except Movie.DoesNotExist:
            return redirect('uweflixapp:profile-list')


method_decorator(login_required, name='dispatch')
class SeatList(View):
    """View for showing the screen and seat arrangement, to book tickets"""

    def get(self, request, showing_id, *args, **kwargs):
        """Renders moviedetail.html with data from DB.

        Shows a discount for tickts if logged into staff member or club rep
        account, discount is set in DB.
        """
        showing = Showing.objects.get(uuid=showing_id)
        seats = showing.seats
        tally = ""
        screen = showing.screen
        price = showing.price
        discount = request.user.discount
        social_distance = showing.COVID_toggle
        movie = showing.movie

        # Apply ticket discount to applicable users.
        if request.user.is_staff or request.user.is_rep:
            price = f"{round(price - (price * (discount / 100)), 2)}"
            price = price + f"({discount}% Club discount applied!)" if discount !=0 else price

        # Reduce seats by half if social distancing is enabled.
        for x in range(seats):
            tally = tally + "1"
        if social_distance:
            tally = tally[:len(tally)//2]
            print(tally)

        context = {
            'seats': tally,
            'screen': screen,
            'price': price,
            'social_distance': social_distance,
            'movie': movie
        }

        return render(request, 'seatlist.html', context)


class RegisterView(CreateView):
    """Shows registration view for creating new accounts."""
    form_class = RegisterForm
    template_name = 'accounts/register.html'
    success_url = '/login/'
