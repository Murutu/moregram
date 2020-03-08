from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(models.Model):
   profile_pic = models.ImageField(upload_to='photos/',null=True)
   fullname = models.CharField(max_length=200,null=True)
   username = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')
   bio = models.TextField(max_length=100)
   email = models.EmailField(null=True)
   phonenumber = models.IntegerField(null=True)