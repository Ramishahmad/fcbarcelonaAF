from django.shortcuts import redirect, render
from django.db.models import Q
from message.models import Conversation, Messages, User
from django.utils import timezone

# Create your views here.

def conversationList(request):
    user = request.user.id
    conversation_list = Conversation.objects.filter(Q(person1_id=user)|Q(person2_id=user))

    context = {
        'conversation_list':conversation_list
    }
    return render(request,'messages/index.html',context)

def messageList(request,cid):
    messages = Messages.objects.filter(conversation_id=cid)
    conversation = Conversation.objects.get(id=cid)
    user = request.user.id

    receiver = 0
    receiver1 = 0
    if user == conversation.person1.id:
        receiver = conversation.person2.id
    elif user == conversation.person2.id:
        receiver = conversation.person1.id
    

# -- code to find last message of this conversation --
    # for items in messages:
    #     receiver1 = items.sender.id
    if messages.last():
        receiver1 = messages.last().sender.id

# code to check last message sender id
    if not user == receiver1:
        conversation.is_read = True
        conversation.save()

    users = User.objects.get(id=receiver)

    if request.method =='POST':
        user = request.user.id
        content = request.POST.get('msg')

        message = Messages.objects.create(sender_id=user,receiver_id=receiver,content=content,conversation_id=cid)
        message.save()
        conversation.timestamp = timezone.now()
        conversation.is_read = False
        conversation.sender = user
        conversation.save()

    context = {
        'messages':messages,
        'users':users
    }

    return render(request,'messages/chat.html',context)


def users(request):
    user = User.objects.all().exclude(id=request.user.id)
    context = {
        'user':user
    }
    return render(request,'messages/user.html',context)


def conv(request,uid):
    user = request.user.id
    receiver = uid
    try:
        conversation = Conversation.objects.get(Q(person1=user,person2=receiver) | Q(person2=user,person1=receiver))
        return redirect('/messages/{}'.format(conversation.id))

    except:
            new_conversation = Conversation.objects.create(person1_id=user,person2_id=receiver)
            new_conversation.save()
            new_conversation = new_conversation
            return redirect('/messages/{}'.format(new_conversation.id))
    