from django.urls import path, include
from . import views

app_name = 'house'
urlpatterns=[
    path('detail/<int:house_id>/',views.detail,name='detail'),
]