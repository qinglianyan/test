from django.db import models

class hourse(models.Model):
    type=(
        ("single","单人间"),
        ("double","双人间"),
        ("triple","三人间"),
        ("quad","四人间")
    )
    orientation=(
        ("north","北"),
        ("east","东"),
        ("west","西"),
        ("south","南")
    )

    hoursename = models.CharField(max_length=32)
    area = models.DecimalField(max_digits=6,decimal_places=2)
    location = models.CharField(max_length=64)
    type = models.CharField(max_length=32,choices=type)
    orientation = models.CharField(verbose_name="朝向",max_length=32,choices=orientation)
    rental = models.IntegerField(verbose_name="租金")
    elevator = models.BooleanField()
    introduction = models.CharField(verbose_name="简介",max_length=256,default="暂无简介")

    User = models.ForeignKey("login.User",on_delete=models.CASCADE,default=None)


