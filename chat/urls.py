from django.urls import path

from chat.views import index, messageList




urlpatterns = [
    path('<int:rid>/',index),
    path('',messageList)
]

