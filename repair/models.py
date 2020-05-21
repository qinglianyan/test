from django.db import models

class repairOrder(models.Model):
    repair_ownUser = models.ForeignKey("login.User",on_delete=models.CASCADE,related_name='repair_ownUser',verbose_name="房东",default=None)
    repair_paidUser = models.ForeignKey("login.User",on_delete=models.CASCADE,related_name='repair_paidUser',verbose_name="房客",default=None)
    house = models.ForeignKey("house.hourse",on_delete=models.CASCADE,default=None)