
from mysite.views import  customisation, dashboard_slider, deletePost, deleteSlider, updatePost, updateSlider
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
    path('customisation',customisation, name='customisation')

]
