from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome,name = 'Welcome to Instagram '),
    path('search/', views.search_results, name='search_results'),
    
]

