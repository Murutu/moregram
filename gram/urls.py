from django.conf import settings
from django.conf.urls.static import static
from django.urls import path,re_path
from . import views

urlpatterns = [
    path('',views.welcome,name = 'welcome'),
    path('search/', views.search_results, name='search_results'),
    path('profile.user.id/<int:user_id=current_user.id>',views.profile, name = 'profile'),
    path('new/post',views.new_post, name ='new-post'),
    path('accounts/update-profile/',views.update_profile,name = 'update-profile'),
    path('comment/<int:id>/',views.new_comment, name ='new_comment')
    
]

if settings.DEBUG:
    urlpatterns+= static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)


