from django.urls import path, include

from . import views

urlpatterns =[
    path('',views.ins,name='ins'),
    path('login/',views.login,name='login'),
    path('login/register/',views.register,name='register'),
    path('index/',views.index,name='index'),
]