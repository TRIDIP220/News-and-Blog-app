from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
import requests
from app1.models import *
API_KEY = '67b01fdd60af4dc5805d7727c6b92e77'

@login_required(login_url='login')
def HomePage(request):
     country = request.GET.get('country')
     category = request.GET.get('category')
     if country:
        url = f'https://newsapi.org/v2/top-headlines?country={country}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']
     else:
        url = f'https://newsapi.org/v2/top-headlines?category={category}&apiKey={API_KEY}'
        response = requests.get(url)
        data = response.json()
        articles = data['articles']



     context = {
        'articles' : articles
    }

     return render(request, 'home.html', context)
  

def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confrom password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        



    return render (request,'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def blog(request):
    return render(request,'Blog.html')


def action(request):
    u= Weather()
    u.Name = request.GET['Name']
    u.blogTopics = request.GET['blogTopics']
    u.blog = request.GET['blog']
    u.save()
    return render(request,'Blog.html')


def show(request):
    x = Weather.objects.all()

    return render(request,'Show.html',{'x':x})

def Del(request,id):
    x = Weather.objects.get(id =id)
    x.delete()
    return redirect('../show')





    