from django.shortcuts import render
from .models import Post,Profile,Comment,Like
from django.http import HttpResponse
# Create your views here.
def welcome(request):
    posts = Post.objects.all().order_by("-id")
    profiles = Profile.objects.all()
    current_user = request.user
    
    comments=Comment.objects.all()
    likes = Like.objects.all()
    
    return HttpResponse('Welcome to MoreGram')
