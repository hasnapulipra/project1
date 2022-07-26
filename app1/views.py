from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
# def fun1(request):
#     return HttpResponse("hello")

def fun2(request):
    return render(request,'index.html')

def fun3(request):
    return render(request,'page1.html')

def fun4(request):
    return render(request,'profile.html')