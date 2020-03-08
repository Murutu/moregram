from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Profile(model.Model):
   profile_pic = models.ImageField(upload_to='photos/',null=True)
   fullname = models.CharField(max_length=255,null=True)
   username = models.OneToOneField(User,on_delete=models.CASCADE,related_name='profile')