
from django.db import models

# Create your models here.
class Student(models.Model):
    # shomara = models.IntegerField(max_length=20)
    # id = id
    
    name = models.CharField(max_length=20)
    age = models.IntegerField()
    salary = models.IntegerField()

    def __str__(self):
        return "Name: {} ".format(self.name,self.id)

class Login(models.Model):
    # shomara = models.IntegerField(max_length=20)
    # id = id
    
    uname = models.CharField(max_length=20)
    pwd = models.CharField(max_length=20)
    # salary = models.IntegerField()
    def __str__(self):
        return "Name: {} ".format(self.uname)
class slider(models.Model):
    # shomara = models.IntegerField(max_length=20)
    # id = id
    
    name = models.CharField(max_length=100)
    img_url = models.CharField(max_length=1000)
    # salary = models.IntegerField()
    def __str__(self):
        return "Name: {} ".format(self.name)

class posts(models.Model):

    title = models.CharField(max_length=100)
    img = models.CharField(max_length=1000)
    content = models.TextField(max_length=50000)
    views = models.IntegerField(default=0)
    def __str__(self):
        return "Title: {}  Views: {} ".format(self.title,self.views)
    def view(self):
        self.views += 1
