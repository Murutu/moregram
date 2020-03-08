from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

# Create your models here.
class Profile(models.Model):
   profile_pic = models.ImageField(upload_to='photos/',null=True)
   fullname = models.CharField(max_length=200,null=True)
   username = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
   bio = models.TextField(max_length=100)
   email = models.EmailField(null=True)
   phonenumber = models.IntegerField(null=True)
   
@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
       Profile.objects.create(username=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()

def __str__(self):
    return self.username.username

@classmethod
def search_profile(cls,search_term):
    profiles = cls.objects.filter(Q(username__username=search_term) | Q(fullname__icontains=search_term))
    return profiles

class Post(models.Model):
    photo_pic = models.ImageField(upload_to = 'photos/')
    caption = models.CharField(max_length=3000)
    upload_by = models.ForeignKey(Profile)
    likes = models.IntegerField(default=0)
    post_date=models.DateTimeField(auto_now_add=True)

def __str__(self):
    return self.caption

def save_photo(self, user):
    self.save()

@classmethod
def all_photos(cls):
    all_photos = cls.objects.all()
    return all_photos

@classmethod
def user_photos(cls, username):
    photos = cls.objects.filter(uploaded_by__username=username)
    return photos

@classmethod
def filter_by_caption(cls, search_term):
    return cls.objects.filter(caption__icontains=search_term)

def delete_photo(self, user):
    self.delete()

class Comment(models.Model):
    comment_content = models.CharField(max_length=300)
    username = models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)

def save_comment(self):
    self.save()

class Like(models.Model):
    models.ForeignKey(User,on_delete=models.CASCADE)
    post = models.ForeignKey(Post,on_delete=models.CASCADE)
    control = models.CharField(max_length=50,null=True)

def __str__(self):
    return self.control

def save_like(self):
    self.save()

class Follow(models.Model):
    username = models.ForeignKey(User, related_name='follower')
    followed = models.ForeignKey(User, related_name='followed')
    follow_id = models.CharField(max_length=50,unique=True, null=True)

def __str__(self):
    return self.follow_id

def save_like(self):
    self.save()