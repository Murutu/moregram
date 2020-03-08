from django.shortcuts import render
from .models import Post,Profile,Comment,Like
from django.http import HttpResponse
from .forms import NewsLetterForm
# Create your views here.
def welcome(request):
    posts = Post.objects.all().order_by("-id")
    profiles = Profile.objects.all()
    current_user = request.user
    
    comments=Comment.objects.all()
    likes = Like.objects.all()
    
    for post in posts:
        num_likes=0
        for like in likes:
            if post.id == like.post.id:
                num_likes +=1
                post.likes = num_likes
                post.save
    
    return HttpResponse('Welcome to MoreGram')
