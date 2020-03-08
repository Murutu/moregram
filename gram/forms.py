from django import forms
from .models import Post,Comment
from .models import *


class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    
    
class LikeForm(forms.ModelForm):
    class Meta:
        model=Like
    exclude=['username','post']
    
class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        exclude=['username','post']
        
class NewPostForm(forms.ModelForm):
    class Meta:
        model = Post
        exclude = ['upload_by', 'pub_date','likes','location']
        
        
class ProfileForm(forms.ModelForm):
       def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
       self.fields['fullname'].widget=forms.TextInput()
class Meta:
       model=Profile
       exclude=['username']
