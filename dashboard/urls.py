from django.contrib import admin
from django.urls import path, include
from . import views
from .views import NutrientsData

urlpatterns = [
    path('', views.NutrientsView, name='dashboard'),
    path('home/', views.HomeView, name='home'),
    path('api/nutrients/', NutrientsData.as_view()),
    path('post/', views.PostNutrients, name='post'),
    path('notes/', views.Notes, name='notes'),

    #User authentication
    path('register/', views.UserSignUp, name='register'),
    path('login/', views.UserLogin, name='login'),
    path('logout/', views.UserLogOut, name='logout'),
]