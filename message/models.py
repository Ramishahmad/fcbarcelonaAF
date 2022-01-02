from django.db import models
from django.db.models.deletion import CASCADE
from django.contrib.auth import get_user_model

# Create your models here.

User = get_user_model()

class Conversation(models.Model):

    person1 = models.ForeignKey(User,on_delete=CASCADE,related_name='person1')
    person2 = models.ForeignKey(User,on_delete=CASCADE,related_name='person2')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    sender = models.IntegerField(blank=True,null=True)
    unread = models.IntegerField(default=0)
    seen_time = models.DateTimeField(null=True,blank=True)

    def __str__(self):
        return 'ID: {} - between: {} and {}  -- Time: ( {} )'.format(self.id,self.person1.name,self.person2.name,self.timestamp)

    class Meta:
        ordering = ['-timestamp']



class Messages(models.Model):

    sender = models.ForeignKey(User,on_delete=CASCADE,related_name='sender')
    receiver = models.ForeignKey(User,on_delete=CASCADE,related_name='receiver')
    content = models.CharField(max_length=1000)
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)
    conversation = models.ForeignKey(Conversation,on_delete=CASCADE)
    decoded = models.CharField(max_length=500)

    def __str__(self):
        return 'Conversation ID: {} - From: {} - To: {} - Time: ({}) -'.format(self.conversation.id,self.sender.name,self.receiver.name,self.timestamp)

    class Meat:
        ordering = ['timestamp']