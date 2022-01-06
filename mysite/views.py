from django.contrib import auth
from django.db.models import fields, Q
from django.db.models.expressions import F
from django.forms.utils import to_current_timezone
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, redirect, render
from rest_framework import response
from message.models import Conversation
from .models import  User, comments_replays, logs, posts, slider,comments,FilterComments,Login
from accounts.models import Accounts
from .forms import LoginForm, PostForm, SliderForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import os
from django.utils.timesince import timesince
from website import settings
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model, login,authenticate, logout
from website.settings import BASE_DIR
from rest_framework.decorators import api_view
from rest_framework.response import Response
 

# Global Variables
colapse = ""
num_visits = 0
addnew = " "


# function for temporary posts and is added on context preprocessors
def temporary(request):
    post = posts.objects.all()
    
    for item1 in post:
        if item1.temporary:
            if ('day') in item1.added_on:
                item1.delete()

            elif ('week') in item1.added_on:
                item1.delete()

            elif ('month') in item1.added_on:
                item1.delete()
    return {'hi':'hi'}


# Function for index page
def index(request):
    slide = slider.objects.all()
    post = posts.objects.all()
    user = request.user.id
    conversation_list = Conversation.objects.filter(Q(person1_id=user)|Q(person2_id=user))
    global num_visits

    unread_messages = 0
    for items in conversation_list:
        if not user == items.sender and not items.is_read:
            unread_messages += 1

    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1


    context = {
        'slide':slide,
        'post':post,
        'num_visits':num_visits,
        'unread_messages':unread_messages,
        
    
    }

    return render(request,'website/index1.html',context)


# Function for detail view of post
def singlepost(request,pid):
    
    slide = slider.objects.all()
    post1 = posts.objects.all() 
    post = posts.objects.get(id=pid)
    filtercomment = FilterComments.objects.all()
    # comment = comments_replays.objects.all()
    not_allowed = " "
    filtered_word = " "
    filtered = False
    if request.method == 'POST':
        name1 = request.user.name
        content = request.POST.get('content')
        # name1 = request.user.username

        for items in filtercomment:
            if content in items.name:
                filtered = True

        for items in filtercomment:
            x =  content.find(items.name)
            
            if x != -1:
                filtered= True
                not_allowed = "show"
                filtered_word = items.name
                break
        
        if (content != ""):
            if filtered == False:
                commentnew = comments.objects.create(name=name1,content=content,post=post,user=request.user)
                commentnew.save()
                return HttpResponseRedirect('/post/{}'.format(post.id))

                
        

    
    comment1 = comments.objects.filter(post__id=pid,show_comment=True)

    comment_replay = comments_replays.objects.all()

    post2 = get_object_or_404(posts,id=pid)
    post2.view()
    post2.save()
    views = post2.views
    context = {
        'comment_replay':comment_replay,
        'filtered_word':filtered_word,
        'not_allowed':not_allowed,
        'comments':comment1,
        'slide':slide,
        'post':post,
        'post1':post1, 
        'views':views

    }   
    return render(request,"website/singlepost.html",context)


# function for login page
def login1(request):
    invalid = ""
    error = ""
    Email = ""
    link = request.get_full_path()
    link = link.lstrip("/login/?next=")

    if request.method == 'POST':
        uname = request.POST.get('uname')
        pwd = request.POST.get('pwd')
        user = authenticate(request,username=uname,password=pwd)


        if user is None:
            try:
            
                users = get_user_model().objects.get(email=uname)
                if users:
                    error = "Invalid Password"
                    Email = uname
            except:
                error = "This email does not have account"
                Email = ""

            invalid = "show"
            context = {
            'Email':Email,
            'Error': error,
            'invalid':invalid
            
            }
            return render(request,'dashboard/login.html',context)
    
        login(request,user)
        if link:
            return redirect("/"+link)



        return redirect(reverse_lazy('dashboard'))
    return render(request,'dashboard/login.html')


# function for logout
def logout1(request):
        logout(request)
        return redirect(reverse_lazy('login'))


# Function for dashboard page
@login_required
def dashboard(request):
    post = posts.objects.all()
    slide = slider.objects.all()
    item = []
    # added = posts.objects.all().first().added_on

    # added = added.split()
    # added_on = added.pop(0)     

    # code for temporary posts
    # for item1 in post:
    #     if item1.temporary:
    #         if ('day') in item1.added_on:
    #             item1.delete()

    #         if ('week') in item1.added_on:
    #             item1.delete()

    #         if ('month') in item1.added_on:
    #             item1.delete()

    post_count = 0
    slides_count = 0
    post_views = 0

    for items in slide:
        slides_count += 1

    for item in post:
        item = item

        if item.draft == True:
            item.draft_or_published = 'Draft'
            item.draft_color = 'red'
            post_count -= 1
        else:
            item.draft_or_published = 'Published'
            item.draft_color = 'green'

        post_count = post_count + 1  
        post_views = post_views+item.views          
    
    context = {
        # 'added':added_on,
        'post':post,
        'colapse':colapse,
        'item':item,
        'num_visits':num_visits,
        'post_count':post_count,
        # 'slides':slides, 
        'post_views':post_views,
        'slides_count':slides_count
           }
    return render(request,'dashboard/dashboard.html',context)


# Function to add new post
@login_required
def addPost(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        content = request.POST.get('content')
        draft = request.POST.get('draft')
        priority = request.POST.get('priority')
        temporary = request.POST.get('temporary')

        # print(request.POST)
        post = posts.objects.create(title=title,image=image,content=content)        

        if draft == None:
            post.draft = False
        else:
            post.draft = True


        if priority == None:
            post.priority = False
        else:
            post.priority = True

        if temporary == None:
            post.temporary = False
        else:
            post.temporary = True
            
        post.save()

        return HttpResponseRedirect(reverse_lazy('dashboard'))
    
    context = {
        'form1':form
    }
    return render(request,"dashboard/addpost1.html",context)


# Function to update a post 
@login_required
def updatePost(request,pid):
    s = posts.objects.get(id=pid)
    create_log = ''
    draft_check = ''
    priority_check = ''    
    if s.draft == True:
        draft_check = 'checked'

    if s.priority == True:
        priority_check = 'checked'
    if request.method == 'POST':
        draft = request.POST.get('draft')
        priority = request.POST.get('priority')
        titles = request.POST.get('title')
        contents = request.POST.get('content')
        images = request.FILES['image']
        temporary = request.POST.get('temporary')

        s.title = titles
        s.content = contents
        s.image = images

        if draft == None:
            s.draft = False
        else:
            s.draft = True
            
        if priority == None:
            s.priority = False
        else:
            s.priority = True

        if temporary == None:
            s.temporary = False
        else:
            s.temporary = True
        s.save()
        
        create_log = logs.objects.create(user=request.user.name,post=s)
        create_log.save()
        return HttpResponseRedirect(reverse_lazy('dashboard'))
    
    log = logs.objects.filter(post=s)

    context = {
        's':s,
        'log':log,
        'draft_check':draft_check,
        'priority_check':priority_check,
        'p_title': s.title,
        'p_img': s.image,
        'p_content': s.content,
        'p_id':s.id,
    }
    return render(request,"dashboard/updatepost.html",context)


# Function to delete a post 
@login_required
def deletePost(request,pid):
     s = posts.objects.get(id=pid)
     s.delete()
     return HttpResponseRedirect(reverse_lazy('dashboard'))
    

# Function for slider dashboard
@login_required
def dashboard_slider(request):
        slide = slider.objects.all()
        form = SliderForm(request.POST or None)
        global addnew
        addnew = "display:none;"
        addorupdate = "Add Slide"
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse_lazy('dashboard_slider'))
    
        context = {
        'addorupdate':addorupdate,
        'slide':slide,
        'form':form,
        'addnew':addnew
    }
        return render(request,'dashboard/dashboard_slider.html',context)


# Function to update a slider image
@login_required
def updateSlider(request,sid):
    slide = slider.objects.all()
    s = slider.objects.get(id=sid)
    addnew = " "
    addorupdate = "Update Slide"
    form = SliderForm(request.POST or None,instance=s)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('dashboard_slider'))
    
    context = {
        'addorupdate': addorupdate,
        'slide':slide,
        'form':form,
        's_name': s.name,
        's_img': s.img_url,
        'addnew':addnew
    }
    return render(request,"dashboard/dashboard_slider.html",context)


# Function to delete a slider image 
@login_required
def deleteSlider(request,sid):
     s = slider.objects.get(id=sid)
     s.delete()
     return HttpResponseRedirect(reverse_lazy('dashboard_slider'))


# Function for Comment page 
@login_required
def comments1(request):
     
    comment = comments.objects.all()
    filtercomments = FilterComments.objects.all()


    if request.method == 'POST':
        name = request.POST.get('name')
        filters = FilterComments.objects.create(name=name)
        filters.save()
        return redirect(reverse_lazy('comments'))

        
    context = {
        # 'form':form
        'comments':comment,
        'filters':filtercomments,
     }
    return render(request,"dashboard/comments.html",context)


@login_required
def showComment(request,cid):

    comment = comments.objects.get(id=cid)
    comment.show_comment=True
    comment.show_comments='none'
    comment.show_comment_label =" Published "
    comment.show_comment_color =" green "
    comment.save()
    
    return redirect(reverse_lazy('comments'))


@login_required
def deleteComment(request,cid):
     s = comments.objects.get(id=cid)
     s.delete()
     return HttpResponseRedirect(reverse_lazy('comments'))


@login_required
def deleteCommentFilter(request,fid):
     s = FilterComments.objects.get(id=fid)
     s.delete()
     return HttpResponseRedirect(reverse_lazy('comments'))


@login_required
def clearLogs(request,lid):
    s = posts.objects.get(id=lid)
    log = logs.objects.filter(post=s)
    log.delete()

    return HttpResponseRedirect(reverse_lazy('dashboard'))


@login_required
def manage(request):
    post=posts.objects.all()
    image = os.listdir('media')
    lists = []
    filesize = 0
    sizes = []
    for files in image:
        y = str(post).find(files)

        if y == -1:
            lists.append(files)
            size = os.path.getsize("media/" + files)/1024
            sizes.append(size)  
    
    for nums in sizes:
        filesize += nums

    filesize = "{:.2f}".format(filesize)

    context = {
        'lists':lists,
        'filesize':filesize,
        'sizes':sizes
    }    

    return render(request,'dashboard/manage.html',context)


@login_required
def deleteUnusedImages(request,image):
    os.remove("media/" + image)

    return HttpResponseRedirect(reverse_lazy('manage'))


@login_required
def deleteUnusedImageAll(request):

    post=posts.objects.all()
    image = os.listdir('media')

    for files in image:
        y = str(post).find(files)
        if y == -1:
            os.remove("media/" + files)

    return HttpResponseRedirect(reverse_lazy('manage'))



def replayComment(request):
     
    replay_comment = comments_replays.objects.all()
    
    if request.method == 'POST':
        post_id = request.POST.get('post_id')
        replay_name = request.user.name
        replay_content = request.POST.get('replay_content')
        comment_id = request.POST.get('comment_id')

        if (replay_name != ""):
            if (replay_content != ""):
                    replay_commentnew = comments_replays.objects.create(name=replay_name,content=replay_content,comment_id=comment_id)
                    replay_commentnew.save()
                    return HttpResponseRedirect('/post/{}'.format(post_id))


def add_user(request):
    
    user1 = User.objects.all()
    if request.method == 'POST':
        # title = request.POST.get('title')
        image = request.FILES['image']
        name = request.POST.get('name')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        password = request.POST.get('pwd')

        # print(request.POST)
        users = Accounts.objects.create(name=name,image=image,email=email,gender=gender)        
        users.set_password(password)
        users.is_superuser = True
        users.is_staff = True
        users.save()
        return HttpResponse('Added successfully')
    context = {
        'users':user1
    }
    return render(request,'dashboard/add_account.html',context)