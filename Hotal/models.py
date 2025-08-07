from django.db import models

# Create your models here.
## create class with app_name and models.model inherited their.
class Hotal(models.Model):
    ## create fields here
    Hotal_icon = models.CharField( max_length=50)
    ## data base me field name use their.
    Hotal_title = models.CharField(max_length=50)
    Hotal_des = models.TextField()
## autometicaly create by data base.

# Create your models here.
## create class with app_name and models.model inherited their.
class login(models.Model):
    ## create fields here use charField for any thing you create.
    ## data base use this field name
    login_user = models.CharField( max_length=50)
    login_password = models.CharField( max_length=50)
    
## autometicaly create by data base.