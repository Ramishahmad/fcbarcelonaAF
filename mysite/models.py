from django.db import models
from django.db.models.deletion import CASCADE


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

    title = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    content = models.TextField(max_length=50000)
    views = models.IntegerField(default=0)

    def __str__(self):
        return "Title: {}  Views: {} ".format(self.title,self.views)
        
    def view(self):
        self.views += 1


class comments(models.Model):
    name = models.CharField(max_length=100,null=False)
    content = models.TextField(max_length=500,null=False)
    post = models.ForeignKey(posts,on_delete=CASCADE)
    show_comment = models.BooleanField(default=False)
    show_comments = models.CharField(max_length=10,default='hidden')
    show_comment_label = models.CharField(max_length=20,default='Not Published')
    show_comment_color = models.CharField(max_length=20,default='red')


    def __str__(self):
        return 'name: {} , comment id: {} ,  Post: {} '.format(self.name,self.id,self.post.title)

class FilterComments(models.Model):
    name = models.CharField(max_length=20,default=" ",null=True,blank=True)

    def __str__(self):
        return 'name: {}'.format(self.name)