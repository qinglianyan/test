from django.db import models

class rentOrder(models.Model):
    rent_ownUser = models.ForeignKey("login.User",on_delete=models.CASCADE,related_name='rent_ownUser',verbose_name="房东",default=None)
    rent_paidUser = models.ForeignKey("login.User",on_delete=models.CASCADE,related_name='rent_paidUser',verbose_name="房客",default=None)
    house = models.ForeignKey("house.hourse",on_delete=models.CASCADE,default=None)
