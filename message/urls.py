from django.urls import path

from .views import conv, conversationList, messageList, users




urlpatterns = [
    path('<int:cid>/',messageList),
    path('',conversationList),
    path('users/',users),
    path('users/<int:uid>',conv),
]

