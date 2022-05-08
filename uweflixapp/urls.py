from django.urls import path, include
from .views import Home, MovieList, MovieDetail

app_name = 'uweflixapp'

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('watch/movielist', MovieList.as_view(), name="movie-list"),
    path('watch/detail/<str:movie_id>', MovieDetail.as_view(), name="movie-detail")
    ]
