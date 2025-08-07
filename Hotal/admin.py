from django.contrib import admin
##import file from app
from Hotal.models import Hotal
## impor model and class here\
from Hotal.models import login



##create class with name
class Hotal_login(admin.ModelAdmin):
    ##create tuple and use fields names in it.\
    list_login=('login_user','login_password')
## Register your models in Admin panel
admin.site.register(login,Hotal_login)

## Create class with name
class Hotal_Admin(admin.ModelAdmin):
    ##Create set and use fields names in it.
    list_display=('Hotal_icon','Hotal_title','Hotal_des')
# Register your models here.
admin.site.register(Hotal,Hotal_Admin)