from django.urls import path

from .views import conv, conversationList, messageList, users




urlpatterns = [
    path('<int:cid>/',messageList,name='message_list'),
    path('',conversationList,name='conversation_list'),
    path('users/',users),
    path('users/<int:uid>',conv),
]

