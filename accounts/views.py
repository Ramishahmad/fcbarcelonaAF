from django.http.response import HttpResponse
from django.shortcuts import render
from mysite.models import Accounts
from django.contrib.auth import get_user_model
User = get_user_model()
# Create your views here.


def register(request):
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
        users.save()
        return HttpResponse('Added successfully')
    context = {
        'users':user1
    }
    return render(request,'accounts/register1.html',context)