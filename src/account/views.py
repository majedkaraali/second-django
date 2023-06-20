from django.shortcuts import render,redirect
from django.contrib.auth import login,authenticate,logout
from account.forms import RegisterationForm,AccountAuthenticationForm


# Create your views here.

def registration_view(requset):
    context={}
    if requset.POST:
        form=RegisterationForm(requset.POST)
        if form.is_valid():
            form.save
            email=form.cleaned_data.get('email')
            raw_password=form.cleaned_data.get('password1')
            account=authenticate(email=email,password=raw_password)
            login(requset,account)
    
            return redirect('home')
        else:
            context['registeration_form']=form
    else:
        form=RegisterationForm
        context['registeration_form']=form
    return render(requset,'account/register.html',context)

def logout_view(requset):
    logout(requset)
    return redirect('home')


def login_view(requset):
    context={}

    user=requset.user
    if user.is_authenticated:
        return redirect('home')
    
    if requset.POST:
        form=AccountAuthenticationForm(requset.POST)
        if form.is_valid():
            email=requset.POST['email']
            password=requset.POST['password']
            user=authenticate(email=email,password=password)
            if user:
                login(requset,user)
                return redirect('home')

    else:
        form=AccountAuthenticationForm()
        context['login_form']=form
        return render(requset,'account/login.html',context)