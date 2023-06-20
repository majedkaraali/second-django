from django.shortcuts import render

# Create your views here.

def home_screen(request):
    return render(request,'personel/home.html',{})

def team_view(request):
    return render(request,'personel/team.html',{})

def about_view(request):
    return render(request,'personel/about.html',{})


