from django import forms
from .models import Login, comments, posts,slider


# Form for post to add or update
class PostForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = [
            # 'id',
            'title',
            'image',
            'thumbnail',
            'content'
            
        ]


# Form to add or update slider images 
class SliderForm(forms.ModelForm):
    class Meta:
        model = slider
        fields = [
            # 'id',
            'name',
            'img_url',
            # 'content'
            
        ]

# Form for login 
class LoginForm(forms.Form):
    uname = forms.CharField(label='User Name',max_length=20)
    pwd = forms.CharField(label='Password',max_length=20)

        