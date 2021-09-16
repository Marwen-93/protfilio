from django.shortcuts import render

# Create your views here.

def profile(request):
    return render(request,'blog/profile.html')

def education (request):
    return render(request,'blog/education.html')