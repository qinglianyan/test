from django.db import models

class repairOrder(models.Model):
    begintime = models.DateField(auto_now_add=True, verbose_name="开始时间")
    overtime = models.DateField(default=None, verbose_name="结束时间")
    repair_ownUser = models.ForeignKey("login.User",on_delete=models.CASCADE,related_name='repair_ownUser',verbose_name="房东",default=None)
    repair_paidUser = models.ForeignKey("login.User",on_delete=models.CASCADE,related_name='repair_paidUser',verbose_name="房客",default=None)
    house = models.ForeignKey("house.house",on_delete=models.CASCADE,default=None)
    content = models.CharField(verbose_name="投诉内容",max_length=256)