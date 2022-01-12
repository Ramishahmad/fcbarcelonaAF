from django.urls import path
from django.views.generic.base import TemplateView

from api.views import (comment_replay_serializer, comment_serializer, 
        filter_comment_serializer, message_list_serializer, post_comment_serializer, posts_serializer, 
        single_post_serializer, single_user_serializer, slider_serializer )


app_name = 'api'

urlpatterns = [
    path('posts/',posts_serializer),
    path('post/<int:pid>',single_post_serializer),
    path('post-comment/<int:pid>',post_comment_serializer),
    path('slider/',slider_serializer),
    path('filter-comment/',filter_comment_serializer),
    path('comment/',comment_serializer),
    path('comment-replay/<int:pid>',comment_replay_serializer),
    path('user/<int:uid>',single_user_serializer),
    path('messages/<int:cid>',message_list_serializer),

    # these urls are for testing after test complete they will be deleted
    path('index/',TemplateView.as_view(template_name='api/index.html')),
]