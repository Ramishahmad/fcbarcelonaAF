from abc import abstractmethod
from django.db.models import fields, Q
from django.shortcuts import get_object_or_404, redirect, render
from .models import  User, logs, posts, slider,comments,FilterComments,Login
from .forms import LoginForm, PostForm, SliderForm
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
import os
from website import settings


# Global Variables
colapse = ""
num_visits = 0
slides = 0
addnew = " "

# Function for index page
def index(request):
    slide = slider.objects.all()
    post = posts.objects.all()
    global num_visits
    num_visits = request.session.get('num_visits',0)
    request.session['num_visits'] = num_visits + 1
    global slides
    slides = 0
    for i in slide:
        slides = slides + 1
    context = {
        'slide':slide,
        'post':post,
        'num_visits':num_visits
        
    
    }

    return render(request,'mysite/index1.html',context)


# Function for detail view of post
def singlepost(request,pid):
    
    slide = slider.objects.all()
    post1 = posts.objects.all() 
    post = posts.objects.get(id=pid)
    filtercomment = FilterComments.objects.all()
    not_allowed = " "
    filtered_word = " "
    filtered = False
    if request.method == 'POST':
        name1 = request.POST.get('name')
        content = request.POST.get('content')
        # name1 = request.user.username

        # for items in filtercomment:
        #     if content in items.name:
        #         filtered = True

        for items in filtercomment:
            x =  content.find(items.name)
            
            if x != -1:
                filtered= True
                not_allowed = "show"
                filtered_word = items.name
                break
        
        if (name1 != ""):
            if (content != ""):
                if filtered == False:
                    commentnew = comments.objects.create(name=name1,content=content,post=post)
                    commentnew.save()
                    return HttpResponseRedirect('/post/{}'.format(post.id))
                
        

    
    comment = comments.objects.filter(post__id=pid,show_comment=True)
    
    post2 = get_object_or_404(posts,id=pid)
    post2.view()
    post2.save()
    views = post2.views

    context = {
        'filtered_word':filtered_word,
        'not_allowed':not_allowed,
        'comments':comment,
        'slide':slide,
        'post':post,
        'post1':post1, 
        'views':views

    }   
    return render(request,"mysite/singlepost.html",context)


# function for login page
def login1(request):
    
    invalid = ""
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            
            uname = form['uname'].value()
            pwd = form['pwd'].value()
        s = Login.objects.all()
    try:
        for item in s:
            if uname == item.uname and pwd == item.pwd:
                
                global colapse
                colapse =  "show"
                
                return HttpResponseRedirect(reverse_lazy('dashboard'))
            else:
                invalid = "show"
                colapse = ""

    except:
        pass

    context = {
        'invalid':invalid,
        'colapse':colapse,
    }
    return render(request,'mysite/login.html',context)


# Function for dashboard page
def dashboard(request):
    post = posts.objects.all()
    post_count = 0
    post_views = 0
    for item in post:
        item = item
        post_count = post_count + 1  
        post_views = post_views+item.views          
    
    context = {
        'post':post,
        'colapse':colapse,
        'item':item,
        'num_visits':num_visits,
        'post_count':post_count,
        'slides':slides, 
        'post_views':post_views
           }
    return render(request,'mysite/dashboard.html',context)


# Function to add new post
def addPost(request):
    form = PostForm(request.POST or None)
    if request.method == 'POST':
        title = request.POST.get('title')
        image = request.FILES['image']
        content = request.POST.get('content')

        post = posts.objects.create(title=title,image=image,content=content)
        post.save()
        return HttpResponseRedirect(reverse_lazy('dashboard'))
    
    context = {
        'form1':form
    }
    return render(request,"mysite/addpost1.html",context)


# Function to update a post 
def updatePost(request,pid):
    s = posts.objects.get(id=pid)
    form = PostForm(request.POST or None,instance=s)
    create_log = ''
    if form.is_valid():
        form.save()
        create_log = logs.objects.create(user=request.user.username,post=s)
        create_log.save()
        return HttpResponseRedirect(reverse_lazy('dashboard'))
    
    log = logs.objects.filter(post=s)

    context = {
        'log':log,
        'form1':form,
        'p_title': s.title,
        'p_img': s.image,
        'p_content': s.content,
        'p_id':s.id,
    }
    return render(request,"mysite/updatepost.html",context)


# Function to delete a post 
def deletePost(request,pid):
     s = posts.objects.get(id=pid)
     s.delete()
     return HttpResponseRedirect(reverse_lazy('dashboard'))
    

# Function for slider dashboard
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
        return render(request,'mysite/dashboard_slider.html',context)


# Function to update a slider image
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
    return render(request,"mysite/dashboard_slider.html",context)


# Function to delete a slider image 
def deleteSlider(request,sid):
     s = slider.objects.get(id=sid)
     s.delete()
     return HttpResponseRedirect(reverse_lazy('dashboard_slider'))


# Function for Comment page 
def comments1(request):
     
    comment = comments.objects.all()
    filtercomments = FilterComments.objects.all()


    if request.method == 'POST':
        name = request.POST.get('name')
        filters = FilterComments.objects.create(name=name)
        filters.save
        return redirect(reverse_lazy('comments'))
    # show_comment = comments.objects.filter(show_comment=True)
    # show_comments = "none"
    # if (show_comment==True):
    #     show_comments = "hidden"

        
    context = {
        # 'form':form
        'comments':comment,
        'filters':filtercomments,
     }
    return render(request,"mysite/comments.html",context)


def showComment(request,cid):

    comment = comments.objects.get(id=cid)
    comment.show_comment=True
    comment.show_comments='none'
    comment.show_comment_label =" Published "
    comment.show_comment_color =" green "
    comment.save()
    
    return redirect(reverse_lazy('comments'))


def deleteComment(request,cid):
     s = comments.objects.get(id=cid)
     s.delete()
     return HttpResponseRedirect(reverse_lazy('comments'))


def deleteCommentFilter(request,fid):
     s = FilterComments.objects.get(id=fid)
     s.delete()
     return HttpResponseRedirect(reverse_lazy('comments'))


def clearLogs(request,lid):
    s = posts.objects.get(id=lid)
    log = logs.objects.filter(post=s)
    log.delete()

    return HttpResponseRedirect(reverse_lazy('dashboard'))


def manage(request):
    post=posts.objects.all()
    image = os.listdir('media')
    lists = []
    for files in image:
        y = str(post).find(files)

        if y == -1:
            lists.append(files)
    

    # list1 = set(lists)
    # print(list1)

    context = {
        'lists':lists
    }    

    return render(request,'mysite/manage.html',context)


def deleteUnusedImages(request,image):
    os.remove("media/" + image)

    return HttpResponseRedirect(reverse_lazy('manage'))



def deleteUnusedImageAll(request):

    post=posts.objects.all()
    image = os.listdir('media')

    for files in image:
        y = str(post).find(files)
        if y == -1:
            os.remove("media/" + files)

    return HttpResponseRedirect(reverse_lazy('manage'))
