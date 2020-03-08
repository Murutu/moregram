from django.shortcuts import render,redirect
from .models import Post,Profile,Comment,Like
from django.http import HttpResponse
from .forms import NewsLetterForm,LikeForm
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
                post.save()
                
    if request.method == 'POST' and 'liker' in request.POST:
        post_id = request.POST.get("liker")
        likeform = LikeForm(request.POST)
        if likeform.is_valid():
            post_id = int(request.Post.get("liker"))
            like = likeform.save(commit=False)
            like.username = request.user
            like.post = post
            like.control = str(like.username.id)+"-"+str(like.post.id)
            like.save()
            print("like saved")
            return redirect("welcome")
        else:
            likeform = LikeForm()
    
    return HttpResponse('Welcome to MoreGram')
