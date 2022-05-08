from django.urls import path, include
from .views import Home, MovieList, ProfileList, ProfileCreate, MovieDetail

app_name = 'uweflixapp'

urlpatterns = [
    path('', Home.as_view(), name="Home"),
    path('profiles/', ProfileList.as_view(), name="profile-list"),
    path('profiles/create', ProfileCreate.as_view(), name="profile-create"),
    path('watch/<str:profile_id>', MovieList.as_view(), name="movie-list"),
    path('watch/detail/<str:movie_id>', MovieDetail.as_view(), name="movie-detail")
    ]
