from django.db.models import fields
from django.shortcuts import get_object_or_404, render
from .models import Student, posts, slider
from .forms import LoginForm, PostForm, SliderForm
from django.http import HttpResponseRedirect
from .models import Login

# Create your views here.

# Global Variables
colapse = ""
num_visits = 0
slides = 0
addnew = " "

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
                # break
                
                return HttpResponseRedirect('/dashboard')
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


def studentlist(request):
    slist = Student.objects.all()
    context = {
        'slist':slist,
        'colapse':colapse
    }
    
    return render(request,"studentmodule/list.html",context)
    
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

def addPost(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/dashboard')
    
    context = {
        'form1':form
    }
    return render(request,"mysite/addpost1.html",context)



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

def addStudent(request):
    form = PostForm(request.POST or None)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/student/')
    context = {
        'form':form
    }
    return render(request,"studentmodule/create.html",context)


def dashboard_slider(request):
        slide = slider.objects.all()
        form = SliderForm(request.POST or None)
        global addnew
        addnew = "display:none;"
        addorupdate = "Add Slide"
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/dashboard-slider')
    
        context = {
        'addorupdate':addorupdate,
        'slide':slide,
        'form':form,
        'addnew':addnew
    }
        return render(request,'mysite/dashboard_slider.html',context)

def updateSlider(request,sid):
    slide = slider.objects.all()
    s = slider.objects.get(id=sid)
    addnew = " "
    addorupdate = "Update Slide"
    form = SliderForm(request.POST or None,instance=s)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/dashboard-slider')
    
    # form.fields['title'].initial = 'asdasdasd'
    context = {
        'addorupdate': addorupdate,
        'slide':slide,
        'form':form,
        's_name': s.name,
        's_img': s.img_url,
        'addnew':addnew
    }
    return render(request,"mysite/dashboard_slider.html",context)

def deleteSlider(request,sid):
     s = slider.objects.get(id=sid)
    #  form = StudentForm(request.GET,instance=s)
     s.delete()
     return HttpResponseRedirect('/dashboard-slider')
        
     context = {
        # 'form':form
     }


def updateStudent(request,sid):
    s = Student.objects.get(id=sid)
    form = PostForm(request.POST or None,instance=s)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/student/')
    

    context = {
        'form':form
    }
    return render(request,"studentmodule/create.html",context)


def updatePost(request,pid):
    s = posts.objects.get(id=pid)
    form = PostForm(request.POST or None,instance=s)
    if form.is_valid():
        form.save()
        return HttpResponseRedirect('/dashboard')
        
    form.fields['title'].initial = 'asdasdasd'
    context = {
        'form1':form,
        'p_title': s.title,
        'p_img': s.img,
        'p_content': s.content,
    }
    return render(request,"mysite/addpost1.html",context)


def deletePost(request,pid):
     s = posts.objects.get(id=pid)
    #  form = StudentForm(request.GET,instance=s)
     s.delete()
     return HttpResponseRedirect('/dashboard/')
        
     context = {
        # 'form':form
     }
    #  return render(request,"/student/",context)

# def check(request,uname,pwd):
#      s = Student.objects.all()
     
#      form = StudentForm(request.GET,instance=s)
#      s.delete()
#      return HttpResponseRedirect('/student/')


def customisation(request):
     
        
     context = {
        # 'form':form
     }
     return render(request,"mysite/customisation.html",context)
