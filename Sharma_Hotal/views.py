##Import file first and  for Render
from django.shortcuts import render


def Hotal(request):
    return render(request,'index.html')
def home(request):

    return render(request,'app_home.html')
