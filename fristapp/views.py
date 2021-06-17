from django.shortcuts import render
from fristapp.forms import  studemform
from django.http import HttpResponse
from fristapp.models import  student,usercreation
from django.shortcuts import render, redirect
# Create your views here.
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.contrib.auth.hashers import make_password
from django.contrib import messages


def home(request):
    if request.session.has_key('user_email'):
        # print(request.session['user_email'])
        user_mali = request.session['user_email']
        id = usercreation.objects.get(user_email=user_mali)
        data=student.objects.filter(st_id=id.id).order_by('name')
        return render(request,'home.html',{'data':data,'id':id})
    else:
        return redirect('login')

def student_data(request):
    if request.method == 'POST':
        form = studemform(request.POST, request.FILES)
        if form.is_valid():
            obj = form.save(commit=False)
            user_mali=request.session['user_email']
            id=usercreation.objects.get(user_email=user_mali)
            # print('*********************************',id.id)
            obj.st_id=id.id
            obj.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, "newcontact Was Successfull created")
            return redirect('home')
    else:
        form = studemform()
    return render(request, 'form.html', {'form': form})

def student_data_update(request, id):
    obj = student.objects.get(id=id)
    form = studemform(instance=obj)
    if request.method == 'POST':
        form = studemform(data=request.POST, files=request.FILES, instance=obj)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            messages.add_message(request, messages.SUCCESS, "Contact Deqatils Successfull updaate")
            return redirect('home')
    return render(request, 'form.html',{'form':form})


def student_data_delete(request,id):
    obj=student.objects.get(id=id)
    obj.delete()
    messages.add_message(request, messages.SUCCESS, "Contact  Successfull Deleted")
    return redirect('home')



from  fristapp.forms import usercreationform,studemform,loginform
def index(request):
    return  render(request,'index.html')

from django.contrib.auth.hashers import make_password
def user_regisration(request):
    if request.method == 'POST':
        form =usercreationform(request.POST, request.FILES)
        if form.is_valid():
            # obj=form.save(commit=False)
            # print('********************')
            # print(obj.user_password)
            # print(make_password(obj.user_password))
            # obj.user_password=make_password(obj.user_password)
            # obj.save()
            form.save()
            messages.add_message(request, messages.SUCCESS, "Acount Created Successfull  Please Login")
            return redirect('login')
    else:
        form = usercreationform()
    return render(request, 'sign_up.html', {'form': form})

def login(request):
    if request.method == 'POST':
        email=request.POST.get('email')
        pasword=request.POST.get('password')
        try:
            obj=usercreation.objects.get(user_email=email)
            if obj.user_password == pasword:
                request.session['user_email'] = obj.user_email
                return redirect('home')
            else:
                messages.add_message(request, messages.SUCCESS, "Wrong Credtials were provided")
                return redirect('login')
        except:
            messages.add_message(request, messages.SUCCESS, "Acount Not Found Please Register")
            return redirect('index')
    else:
        form = loginform()
        messages.add_message(request, messages.SUCCESS, "Please Do Login")
        return render(request, 'login.html', {'form': form})


def logout(request):
    del(request.session['user_email'])
    messages.add_message(request, messages.SUCCESS, "Logout Successfull  Please Login Again")
    return redirect('login')