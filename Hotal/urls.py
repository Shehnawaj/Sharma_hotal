## App name import
from Hotal import views
## import path or urls
from django.urls import path
urlpatterns = [
    path('page/',views.firstpage),
    path('home/',views.home),
    path('login/',views.login),
    path('thank/',views.thank,name='thank')

]