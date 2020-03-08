from django.urls import path
from . import views

urlpatterns = [
    path('',views.welcome,name = 'Welcome to MoreGram '),
    path('search/', views.search_results, name='search_results'),
    path('accounts/profile/(\d+)',views.profile, name = 'profile'),
    path('new/post',views.new_post, name ='new-post'),
    path('accounts/edit-profile/',views.edit_profile,name = 'edit-profile'),
    
]

