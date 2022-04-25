from django.urls import path
from . import views

#app_name = 'uweflixapp'

urlpatterns = [
    path('register/', views.registerPage, name="register"),
    path('login/', views.loginPage, name="login"),
    path('logout/', views.logoutUser, name="logout"),

    path('', views.home, name="home"),
    path('films/', views.films, name="films"),
    path('customer/', views.customer, name="customer"),
    path('showings/', views.showings, name="showings"),
    path('clubs/', views.clubs, name="clubs"),

    path('add_film/', views.addFilm, name="add_film"),
    path('add_showing/', views.addShowing, name="add_showing"),
    path('add_club/', views.addClub, name="add_club"),
    path('delete_film/<str:pk>/', views.deletesFilm, name="delete_film"),

    path('view_showings/', views.viewShowings, name="view_showings"),
    path('select_showing/', views.selectShowing, name="select_showing"),
]