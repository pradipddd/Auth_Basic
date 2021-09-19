from django.urls import path
from .views import homeview,change_password,Userregister,Userlogin,Userlogout

urlpatterns=[
    path('home/',homeview,name='home'),
    path('register/',Userregister,name='register'),
    path('login/',Userlogin,name='login'),
    path('logout/',Userlogout,name='logout'),
    path('change_password/',change_password,name='change_password'),

]