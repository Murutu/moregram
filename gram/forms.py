from django import forms
from .models import *

class NewsLetterForm(forms.Form):
    your_name = forms.CharField(label='First Name',max_length=30)
    email = forms.EmailField(label='Email')
    
    
class LikeForm(forms.ModelForm):
    class Meta:
        model=Like
    exclude=['username']