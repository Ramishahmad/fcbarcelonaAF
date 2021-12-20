from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model
from django.utils.timesince import timesince
from django.contrib.auth import decorators

from accounts.models import Accounts

User = get_user_model()


# Table for login 
class Login(models.Model):
    
    uname = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)

    def __str__(self):
        return "Name: {} ".format(self.uname)


# Table for slider 
class slider(models.Model):
    
    name = models.CharField(max_length=100)
    img_url = models.CharField(max_length=1000)

    def __str__(self):
        return "Name: {} ".format(self.name)


# Table for posts 
class posts(models.Model):

    
    class Meta:
        ordering = ['priority','date']

    title = models.CharField(max_length=100)
    image = models.ImageField(null=True,blank=True)
    content = models.TextField(max_length=50000)
    views = models.IntegerField(default=0)
    date = models.DateTimeField(auto_now_add=True)
    update = models.DateTimeField(auto_now=True)
    draft = models.BooleanField(default=False,blank=True)
    priority = models.BooleanField(default=False,blank=True)
    temporary = models.BooleanField(default=False,blank=True)

    def __str__(self):
        return "Title: {}  Views: {}  image: {}".format(self.title,self.views,self.image.name)
        
    @property
    def added_on(self):

        times = timesince(self.update)
    #     if self.temporary:
            
    #         if 'minute' in times:
    #             self.delete()

    #         if 'week' in times:
    #             self.delete()

    #         if 'month' in times:
    #             self.delete()
        return times


    def view(self):
        self.views += 1


# Table for Comments
class comments(models.Model):
    name = models.CharField(max_length=100,null=True,blank=True)
    content = models.TextField(max_length=500,null=False)
    post = models.ForeignKey(posts,on_delete=CASCADE)
    show_comment = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)
    show_comments = models.CharField(max_length=10,default='hidden')
    show_comment_label = models.CharField(max_length=20,default='Pending Review')
    show_comment_color = models.CharField(max_length=20,default='red')
    user = models.ForeignKey(User,on_delete=CASCADE)

    def __str__(self):
        return 'name: {} , comment id: {} ,  Post: {} '.format(self.name,self.id,self.post.title)


# Table for comment replays
class comments_replays(models.Model):
    name = models.CharField(max_length=100,null=False)
    content = models.TextField(max_length=500,null=False)
    comment = models.ForeignKey(comments,on_delete=CASCADE)
    show_comment = models.BooleanField(default=False)
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return 'name: {} , comment id: {} , ----------- Comment: {} , id: {}'.format(self.name,self.id,self.comment.name,self.comment.id)


# Table for comment filtering
class FilterComments(models.Model):
    
    name = models.CharField(max_length=20,default=" ",null=True,blank=True)

    def __str__(self):
        return 'name: {}'.format(self.name)


# Table for Logs of updated post 
class logs(models.Model):

    class Meta:
        ordering = ['-date']

    date = models.DateTimeField(auto_now_add=True)
    user = models.CharField(max_length=50)
    post = models.ForeignKey(posts,on_delete=CASCADE)

    def __str__(self):
        return 'Last Update: {}, Post: {}'.format(self.date,self.post)