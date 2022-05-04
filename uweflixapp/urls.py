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
    path('screens/', views.screens, name="screens"),
    path('clubs/', views.clubs, name="clubs"),

    path('add_film/', views.addFilm, name="add_film"),
    path('add_showing/', views.addShowing, name="add_showing"),
    path('add_club/', views.addClub, name="add_club"),
    path('add_screen/', views.addScreen, name="add_screen"),
    path('approve_user/<str:pk>/', views.approveUser, name="approve_user"),
    path('delete_film/<str:pk>/', views.deletesFilm, name="delete_film"),
    path('modify_film/<str:pk>/', views.modifyFilm, name="modify_film"),

    path('view_showings/', views.viewShowings, name="view_showings"),
    path('select_showing/<str:pk>/', views.selectShowing, name="select_showing"),
    
    path('view_transactions/', views.viewTransactions, name="view_transactions"),

    #path('create_booking/', views.createBooking, name="create_booking"),
    #path('cancel_booking/', views.cancelBooking, name="cancel_booking"),
]