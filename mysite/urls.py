
from mysite.models import comments
from mysite.views import   comments1, dashboard_slider, deleteComment, deleteCommentFilter, deletePost, deleteSlider, showComment, updatePost, updateSlider
from django.urls import path,include
from mysite.views import index, login1, singlepost, dashboard, addPost



urlpatterns = [
    path('',index, name='index'),
    path('post/<pid>/',singlepost,name="post_url"),
    path('<pid>/delete/',deletePost,name='delete_post'),
    path('<sid>/delete-slider/',deleteSlider,name='delete_slider'),
    path('<pid>/update/',updatePost,name='update_post'),
    path('login/',login1, name='login'),
    path('dashboard/',dashboard, name='dashboard'),
    path('addpost/',addPost, name='add_post'),
    path('dashboard-slider/',dashboard_slider, name='dashboard_slider'),
    path('<sid>/update-slider/',updateSlider,name='update_slider'),
    path('<cid>/show-comment/',showComment,name='show_comment'),
    path('comments',comments1, name='comments'),
    path('<cid>/delete-comment/',deleteComment,name='delete_comment'),
    path('<fid>/delete-comment-filter/',deleteCommentFilter,name='delete_comment_filter'),


]
