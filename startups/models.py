from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()

class StartupsInfo(models.Model):
    CATEGORIES=(
        ("T","Tech"),
        ('A',"Agricultural"),
        ('E','ECommerce'),
        ('M',"Medical"),
        ('O',"Others"),
    )
    startupname=models.CharField(max_length=256,null=False,blank=False)
    category=models.CharField(max_length=1,choices=CATEGORIES,null=False,blank=False)
    description=models.TextField(blank=False,null=False)
    vision=models.TextField(blank=False,null=False)
    startedDate=models.DateTimeField()
    location=models.CharField(max_length=256,null=False,blank=False)
    phone_number=models.CharField(max_length=20,null=False,blank=False)
    phone_number2=models.CharField(max_length=20)
    Datetime=models.DateTimeField(auto_now=True)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

    def __str__(self):
        return self.startupname

class Favourites(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    startup=models.ForeignKey(StartupsInfo,on_delete=models.CASCADE)