from django.db import models


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
