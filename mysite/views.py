from django.db.models import fields, Q
from django.shortcuts import get_object_or_404, render
from .models import  posts, slider
from .forms import LoginForm, PostForm, SliderForm
from django.http import HttpResponseRedirect
from .models import Login
from django.urls import reverse_lazy


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
    post2 = get_object_or_404(posts,id=pid)
    post2.view()
    post2.save()
    views = post2.views
    context = {
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
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('dashboard'))
    
    context = {
        'form1':form
    }
    return render(request,"mysite/addpost1.html",context)


# Function to update a post 
def updatePost(request,pid):
    s = posts.objects.get(id=pid)
    form = PostForm(request.POST or None,instance=s)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect(reverse_lazy('dashboard'))
        
    context = {
        'form1':form,
        'p_title': s.title,
        'p_img': s.img,
        'p_content': s.content,
    }
    return render(request,"mysite/addpost1.html",context)


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


# Function for customisation page 
def customisation(request):
     
        
     context = {
        # 'form':form
     }
     return render(request,"mysite/customisation.html",context)
