from django.contrib.auth import get_user_model
from django.db import models 
from django.db.models.base import Model
from django.db.models.deletion import CASCADE, DO_NOTHING
from django.db.models.fields.related import ForeignKey


User = get_user_model ()
# Create your models here.




class Message(models.Model):


    sender = models.ForeignKey(User,on_delete=CASCADE,related_name='sender_message_set')
    content = models.TextField(max_length=500)
    receiver = models.ForeignKey(User, on_delete=CASCADE,related_name='receiver_message_set')
    timestamp = models.DateTimeField(auto_now_add=True)
    is_read = models.BooleanField(default=False)

    def __str__(self):
        return 'ID : {}  -  From : {} -- To : {}'.format(self.id,self.sender.name,self.receiver.name)

    class Meta:
        ordering = ['timestamp']