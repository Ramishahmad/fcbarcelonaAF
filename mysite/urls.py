
from mysite.models import comments
from mysite.views import   clearLogs, comments1, dashboard_slider, deleteComment, deleteCommentFilter, deletePost, deleteSlider, deleteUnusedImageAll, deleteUnusedImages, manage, replayComment, showComment, updatePost, updateSlider
from django.urls import path,include
from mysite.views import index, login1, singlepost, dashboard, addPost
from django.conf import settings




urlpatterns = [
    # Url of Main Page
    path('',index, name='index'),

    # Url related to Posts
    path('post/<pid>/',singlepost,name="post_url"),
    
    # Url related to login Page
    path('login/',login1, name='login'),

    # Urls related to Dashboard
    path('<pid>/delete/',deletePost,name='delete_post'),
    path('<pid>/update/',updatePost,name='update_post'),
    path('<sid>/delete-slider/',deleteSlider,name='delete_slider'),
    path('<sid>/update-slider/',updateSlider,name='update_slider'),
    path('dashboard/',dashboard, name='dashboard'),
    path('addpost/',addPost, name='add_post'),
    path('dashboard-slider/',dashboard_slider, name='dashboard_slider'),
    path('<cid>/show-comment/',showComment,name='show_comment'),
    path('comments',comments1, name='comments'),
    path('<cid>/delete-comment/',deleteComment,name='delete_comment'),
    path('<fid>/delete-comment-filter/',deleteCommentFilter,name='delete_comment_filter'),

    path('<lid>/clear-log/',clearLogs,name='clear_log'),
    path('<image>/delete-unused-image/',deleteUnusedImages,name='delete_unused_image'),
    path('delete-unused-image-all/',deleteUnusedImageAll,name='delete_unused_image_all'),
    
    path('manage/',manage, name='manage'),

    path('replaycomment/',replayComment, name='replay_comment')



]

