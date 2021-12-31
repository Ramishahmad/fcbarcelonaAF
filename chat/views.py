from django.core.checks import messages
from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from mysite.models import posts
from .models import  User, Message
from django.db.models import Q


# Create your views here.

def messageList(request):
    user = request.user.id
    messages = Message.objects.filter(Q(receiver_id=user) | Q(sender_id=user))

    receivers = []
    for items in messages:
            receivers.append(items.receiver)
    receiver_email = list(set(receivers))
    users = User.objects.all()

    context = {
        'messages':messages,
        'users':users,
        'receiver_email':receiver_email,
    }
    return render(request,'chat/messages.html',context)



def index(request,rid):
    sid = request.user.id
    messages = Message.objects.filter(Q(receiver_id=rid,sender_id=sid) | Q(receiver_id=sid,sender_id=rid))
    receiver = User.objects.get(id=rid)
    

    context = {
        'messages':messages,
        'receiver':receiver
    }
    if request.method == 'POST':
        content = request.POST.get('msg')
        sender = request.user.id
        message = Message.objects.create(receiver_id=rid,sender_id=sender,content=content)
        message.save()

    return render(request,'chat/index.html',context)
