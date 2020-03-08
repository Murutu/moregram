from django import forms
from .models import *
from .models import Post,Comment

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