from django.http.response import HttpResponse
from django.shortcuts import redirect, render
from mysite.models import Accounts
from django.contrib.auth import get_user_model,authenticate,login
User = get_user_model()
# Create your views here.

def register(request):

    user1 = User.objects.all()
    invalid_password = False
    email_exist = False
    if request.user.is_authenticated:
        return redirect('/login')
    if request.method == 'POST':
        # title = request.POST.get('title')
        try:
            image = request.FILES['image']
        except:
            pass
        name = request.POST.get('uname')
        email = request.POST.get('email')
        gender = request.POST.get('gender')
        dob = request.POST.get('dob')
        password = request.POST.get('pass')
        vpassword = request.POST.get('vpass')
        context1 = {}
        user_exist = User.objects.filter(email=email)

        if user_exist:
            email_exist = True
            context2 = {
                'email_exist':email_exist
            }
            return render(request,'accounts/register1.html',context2)
        if not password == vpassword:
            invalid_password = True
            context1 = {
                'invalid_password':invalid_password,

            }
            return render(request,'accounts/register1.html',context1)


        users = Accounts.objects.create(name=name,email=email,gender=gender,date_of_birth=dob)  
        try:
            users.image=image 
        except:
            pass     
        users.set_password(password)
        users.save()
        user = authenticate(request,username=email,password=password)
        login(request,user)
        return redirect('/')

    context = {
        'users':user1,
    }
    return render(request,'accounts/register1.html',context)



def profile(request,uid):
    try:
        user = User.objects.get(id=uid)
    except:
        return redirect('/')
    
    context = {
        'users':user
    }
    return render(request,'accounts/profile.html',context)