from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth import authenticate,login,logout
#from . import forms
#from first_app.models import User
from first_app.forms import UserForm,UserProfileInfoForm
from django.urls import reverse
from django.contrib.auth.decorators import login_required



# Create your views here.
def index(request):
    return render(request,'index.html')


@login_required
def special(request):
    return HttpResponse("You are logged in, Nice!")

@login_required
def user_logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('index'))


'''def form(request):
    form=forms.FormName()
    if request.method=='POST':
        form= forms.FormName(request.POST)

        if form.is_valid():
            print("Validation Success!")
            print("Name:" +form.cleaned_data['name'])
            print("Email:" +form.cleaned_data['Email'])
            print("Message:" +form.cleaned_data['Message'])

    return render(request,'contact.html',{'form':form})

def user(request):
    list_dict = User.objects.order_by('name')
    direct_user = {'user':list_dict}
    return render(request,'user.html',context=direct_user)'''

def work(request):
    return render(request,'work.html')

def register(request):
    registered = False
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)
        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            profile = profile_form.save(commit=False)
            profile.user = user
            if 'profile_pic' in request.FILES:
                print('found it')
                profile.profile_pic = request.FILES['profile_pic']
            profile.save()
            registered = True
        else:
            print(user_form.errors,profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    return render(request,'register.html',
                          {'user_form':user_form,
                           'profile_form':profile_form,
                           'registered':registered})
def result(request):
    return render(request,'result.html')

def user_login(request):
    if request.method =="POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user= authenticate(username=username,password=password)
        if user:
            if user.is_active:
                login(request,user)
                return HttpResponseRedirect(reverse('index'))
            else:
                return HttpResponse("Account not active")

        else:
            print("SomeOne Tried to login and failed!")
            print("Username: {} and password {}". format(username,password))
            return HttpResponse("INVALID REQUEST DETAILS")
    else:
        return render(request,'login.html',{})
