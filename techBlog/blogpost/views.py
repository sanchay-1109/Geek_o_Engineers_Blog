from django.shortcuts import render



def home(request):
    return render(request,'techblog/blogpost/home.html')


def about(request):
    return render(request,'blogpost/about.html')