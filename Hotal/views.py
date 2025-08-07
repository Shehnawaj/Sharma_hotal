from django.shortcuts import render
## import models file
from Hotal.models import Hotal
## impor models file with class name
from Hotal.models import login


# Create your views here.
def firstpage(request):
    return render(request,'app_hotal.html')
def home(request):
    ## Cache Modal class all data into one variable
    Hotal_data = Hotal.objects.all().order_by('-Hotal_title')
    data = {
        'data':Hotal_data
    }
    
    return render(request,'app_home.html',data)


def login(request):
    return render(request,'app_login.html')

def thank(request):
    if request.method=="GET":
        user=request.GET.get('user')
        password=request.GET.get('pw')
        ## create var for save data
        ## var / modal_name /field_name = value_request_name
        save_data=login(login_user=user,login_password=password)
        ## predefine fun for save this use
        save_data.save()
    return render(request,'thenk_page.html')
