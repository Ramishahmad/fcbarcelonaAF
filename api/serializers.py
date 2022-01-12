from django.db.models import fields
from message.models import Conversation, Messages
from mysite.models import (FilterComments, comments,comments_replays, 
                            logs, posts, slider)
from django.contrib.auth import get_user_model

User = get_user_model()

from rest_framework import serializers


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields =['id','name','email','gender','image']



class PostsSerializer(serializers.ModelSerializer):

    class Meta:
        model = posts
        exclude = ['priority','draft','temporary']
        



class SliderSerializer(serializers.ModelSerializer):

    class Meta:
        model = slider
        fields = ['id','name','img_url']




class CommentReplaySerializer(serializers.ModelSerializer):

    class Meta:
        model = comments_replays
        exclude = ['serializer']




class FilterCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = FilterComments
        exclude = ['serializer']




class LogsSerializer(serializers.ModelSerializer):

    class Meta:
        model = logs
        exclude = ['serializer']




class ConversationSerializer(serializers.ModelSerializer):

    class Meta:
        model = Conversation
        exclude = ['serializer']




class MessageSerializer(serializers.ModelSerializer):
    sender = UserSerializer(read_only=True)
    receiver = UserSerializer(read_only=True)
    conversation = ConversationSerializer(read_only=True)
    class Meta:
        model = Messages
        exclude = ['serializer']
        
        


class CommentSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only = True)

    class Meta:
        model = comments
        exclude = ['serializer']
        