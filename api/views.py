from django.contrib.auth.decorators import login_required
from django.core.checks import messages
from django.http import request
from django.http.response import HttpResponse, JsonResponse
from django.shortcuts import redirect, render
from rest_framework import serializers
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.response import Response
from accounts.models import Accounts
from message.models import Conversation, Messages
from mysite.models import FilterComments, comments, comments_replays, posts, slider
from .serializers import CommentReplaySerializer, CommentSerializer, FilterCommentSerializer, MessageSerializer, PostsSerializer, SliderSerializer, User, UserSerializer
import requests
from django.utils import timezone
from django.urls import reverse_lazy
# Create your views here.


@api_view(['GET'])
def posts_serializer(request):
    post = posts.objects.all()
    serializer = PostsSerializer(post,many=True)
    return Response(serializer.data,status=200)

@api_view(['GET','POST'])
def single_post_serializer(request,pid):
    post = posts.objects.get(id=pid)
    serializer = PostsSerializer(post)
    return Response(serializer.data,status=200)



@api_view(['GET'])
def slider_serializer(request):
    slides = slider.objects.all()
    serializer = SliderSerializer(slides, many=True)
    return Response(serializer.data, status=200)



@api_view(['GET'])
def filter_comment_serializer(request):
    filter_comment = FilterComments.objects.all()
    serializer = FilterCommentSerializer(filter_comment, many=True)
    return Response(serializer.data, status=200)


@api_view(['GET'])
def comment_serializer(request):

    comment = comments.objects.all()
    serializer = CommentSerializer(comment, many=True)
    return Response(serializer.data, status=200)



@api_view(['GET'])
def comment_replay_serializer(request,pid):
    comment = comments_replays.objects.filter(post_id=pid)
    serializer = CommentReplaySerializer(comment, many=True)
    return Response(serializer.data, status=200)




@api_view(['GET','PUT'])
def post_comment_serializer(request,pid):
    comment = comments.objects.filter(post_id=pid,show_comment=True)
    serializer = CommentSerializer(comment, many=True)

    if request.method == 'PUT':
        serializer = CommentSerializer(comment,data=request.data)
        if serializer.is_valid():
            serializer.save()
    return Response(serializer.data, status=200)
    



@api_view(['GET'])
def single_user_serializer(request,uid):
    try:
        user = User.objects.get(id=uid)
    except:
        raise NotFound
    serializer = UserSerializer(user)
    if request.user.id == user.id:
        return Response(serializer.data,status=200)
    else:
        return Response({'detail':'You dont have permission to see details'})



@api_view(['GET','POST'])
def message_list_serializer(request,cid):
    try:
        conversation = Conversation.objects.get(id=cid)
    except:
        return redirect('/messages')
    messages = Messages.objects.filter(conversation_id = cid)
    user = request.user.id
    decoding = ''

    for item in messages:
        decoding = item.content
        for i in (('&%42','a'),('$!22','e'),('@)(12','i'),('*%62','o'),('%#72','u')):
            decoding = decoding.replace(*i)
        item.decoded = decoding

    
    receiver = 0
    last_message_sender = 0
    if user == conversation.person1.id:
        receiver = conversation.person2.id
    elif user == conversation.person2.id:
        receiver = conversation.person1.id

    if messages.last():
        last_message_sender = messages.last().sender.id

    if not user == last_message_sender:
        if conversation.is_read == False:
            conversation.seen_time = timezone.now()
        conversation.is_read = True
        conversation.unread = 0
        conversation.save()


    try:
        users = User.objects.get(id=receiver)
    except:
        return redirect('/')
    
    serializer = MessageSerializer(messages,many=True)

    # if request.method =='POST':
    #     user = request.user.id
    #     content = request.POST.get('msg')

    #     # this code is used for encoding messages
    #     encodings = content
    #     for i in (('a','&%42'),('e','$!22'),('i','@)(12'),('o','*%62'),('u','%#72')):
    #         encodings = encodings.replace(*i)
    #     encoding = encodings


    #     message = Messages.objects.create(sender_id=user,receiver_id=receiver,content=encoding,conversation_id=cid)
    #     message.save()
    #     conversation.timestamp = timezone.now()
    #     conversation.is_read = False
    #     conversation.sender = user
    #     conversation.unread += 1
    #     conversation.save()
    #     return redirect('/messages/{}'.format(cid))
    
    return Response(serializer.data,status=200)


    