from django.urls import path, include
from . import views

urlpatterns=[
    path('houses/',views.houses),
    path('house/<int:id>',views.house),
]