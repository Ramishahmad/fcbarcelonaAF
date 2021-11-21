from django import forms
from .models import Login, Student, posts,slider

class PostForm(forms.ModelForm):
    class Meta:
        model = posts
        fields = [
            # 'id',
            'title',
            'img',
            'content'
            
        ]
class SliderForm(forms.ModelForm):
    class Meta:
        model = slider
        fields = [
            # 'id',
            'name',
            'img_url',
            # 'content'
            
        ]

class LoginForm(forms.Form):
    uname = forms.CharField(label='User Name',max_length=20)
    pwd = forms.CharField(label='Password',max_length=20)

        