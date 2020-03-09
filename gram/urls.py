from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.welcome,name = 'Welcome to MoreGram '),
    path('search/', views.search_results, name='search_results'),
    re_path('accounts/profile/(\d+)',views.profile, name = 'profile'),
    path('new/post',views.new_post, name ='new-post'),
    path('accounts/update-profile/',views.update_profile,name = 'update-profile'),
    
]

