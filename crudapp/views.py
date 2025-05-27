from django.shortcuts import render, redirect
from django.http import JsonResponse
from .forms import  customerform
from .models import customer
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate

from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required
def home(request):
    
  form= customerform()  
  info= customer.objects.filter(userid= request.user.id).values()
  if request.method =="POST":
        
        form= customerform(request.POST, request.FILES)
        if form.is_valid():
          form.save()
          
        return JsonResponse(list(info), safe=False)
            
  context = {'info': info}  
  return render(request, 'crudapp/index.html', context)

@login_required
def edit(request, id):
  data= customer.objects.get(id=id)
  context= {'customer': data}
  
  return render(request, 'crudapp/update.html', context)

def update(request):
  userid= request.POST.get('userid')
  customerid= request.POST.get('customerid')
  
  data= customer.objects.get(id=customerid)
  form= customerform(request.POST, request.FILES, instance=data)
  form.save()
    
  return redirect('home')

def deleteData(request, id):
  data= customer.objects.get(id=id)
  data.delete()
  
  return redirect('home')



def signuppage(request):
  
    context={}
    if request.method=="POST":
      name= request.POST.get('name')
      password= request.POST.get('password1')
    
      data= User.objects.create_user(username= name, password=password)
      data.save()
      context={'msg': 'Account Created Successfully. Please Login'}
    
    return render(request, 'crudapp/signup.html', context)  


def loginpage(request):
  
    context={}
    if request.method=="POST":
        UN= request.POST.get("username")
        PS= request.POST.get("password")
  
    
        userdata= authenticate(username=UN,  password=PS)
        if userdata is not None:
          login(request, userdata)
          return redirect('home')
        else:
           context={'msg': 'Invalid Username or password'}
    
    return render(request, 'crudapp/login.html', context) 


def logoutuser(request):
  logout(request)
  return redirect('login')