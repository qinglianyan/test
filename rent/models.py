from django.db import models

class rentOrder(models.Model):

    type=(
        ("short","短期"),
        ("long","长期")

    )

    begintime = models.DateField(auto_now_add=True,verbose_name="开始时间")
    overtime = models.DateField(default=None,verbose_name="结束时间")
    rent_ownUser = models.ForeignKey("login.User",on_delete=models.CASCADE,related_name='rent_ownUser',verbose_name="房东",default=None)
    rent_paidUser = models.ForeignKey("login.User",on_delete=models.CASCADE,related_name='rent_paidUser',verbose_name="房客",default=None)
    house = models.ForeignKey("house.hourse",on_delete=models.CASCADE,default=None)
    judge = models.BooleanField(verbose_name="审核结果",default=False)
    type = models.CharField(verbose_name="类型",max_length=32,choices=type)

