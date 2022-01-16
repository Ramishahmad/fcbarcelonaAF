from django.shortcuts import redirect, render
from django.db.models import Q
from message.models import Conversation, Messages, User
from django.utils import timezone
from django.urls import reverse_lazy
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
    user = request.user.id
    
    # we get try and catch because if the conversation be deleted we dont get error
    try:
        conversation = Conversation.objects.get(id=cid)
    except:
        return redirect(reverse_lazy('conversation_list'))
    
    # This code is used for decoding the messages 
    decoding = ''
    
    # Code for decoding messages 1
    # for item in messages:
    #     decoding = item.content
    #     decoding = decoding.replace('&%42','a')
    #     decoding = decoding.replace('$!22','e')
    #     decoding = decoding.replace('@)(12','i')
    #     decoding = decoding.replace('*%62','o')
    #     decoding = decoding.replace('%#72','u')
    #     item.decoded = decoding


    # code for decoding messages 2
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


    try:
        users = User.objects.get(id=receiver)
    except:
        return redirect(reverse_lazy('conversation_list'))

    # -- code to find sender of last message of this conversation --
    if messages.last():
        last_message_sender = messages.last().sender.id


    # code to check last message sender id and set the seen time to now and conv unread to false
    if not user == last_message_sender:
        if conversation.is_read == False:
            conversation.seen_time = timezone.now()
        conversation.is_read = True
        conversation.unread = 0
        conversation.save()


    if request.method =='POST':
        user = request.user.id
        content = request.POST.get('msg')

        # this code is used for encoding messages
        encodings = content
        for i in (('a','&%42'),('e','$!22'),('i','@)(12'),('o','*%62'),('u','%#72')):
            encodings = encodings.replace(*i)
        encoding = encodings


        message = Messages.objects.create(sender_id=user,receiver_id=receiver,content=encoding,conversation_id=cid)
        message.save()
        conversation.timestamp = timezone.now()
        conversation.is_read = False
        conversation.sender = user
        conversation.unread += 1
        conversation.save()
        return redirect('/messages/{}'.format(cid))

    context = {
        'messages':messages,
        'users':users,
        'conversation':conversation
    }

    return render(request,'messages/chat.html',context)


def users(request):
    user = User.objects.all().exclude(id=request.user.id)
    context = {
        'user':user
    }
    return render(request,'messages/user.html',context)


# when you click on user and click send message this function check
# if the user have already conversation with you it redirect you to that conversation 
# otherwise if you dont have conversation with the user it will create new conversation
def conv(request,uid):
    user = request.user.id
    receiver = uid
    try:
        conversation = Conversation.objects.get(Q(person1=user,person2=receiver) | Q(person2=user,person1=receiver))
        return redirect('/messages/{}'.format(conversation.id))

    except:
            new_conversation = Conversation.objects.create(person1_id=user,person2_id=receiver)
            new_conversation.save()
            # new_conversation = new_conversation
            return redirect('/messages/{}'.format(new_conversation.id))
    