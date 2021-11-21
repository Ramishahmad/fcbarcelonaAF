
from mysite.views import addStudent, customisation, dashboard_slider, deletePost, deleteSlider,studentlist, updatePost, updateSlider, updateStudent
from django.urls import path,include

from mysite.views import index, login1, singlepost, dashboard, addPost

urlpatterns = [
    # path('',studentlist),
    path('',index),
    path('post/<pid>/',singlepost,name="post_url"),
    path('create/',addStudent),
    path('<pid>/delete/',deletePost,name='delete_post'),
    path('<sid>/delete-slider/',deleteSlider,name='delete_slider'),

    # path('<sid>/update/',updateStudent,name='update_student'),
    path('<pid>/update/',updatePost,name='update_post'),
    path('login/',login1),
    path('dashboard/',dashboard),
    path('addpost/',addPost),
    path('dashboard-slider/',dashboard_slider),
    path('<sid>/update-slider/',updateSlider,name='update_slider'),
    path('customisation',customisation)

]
