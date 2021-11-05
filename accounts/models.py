from django.contrib.auth.models import AbstractUser
from django.db import models
from django.utils.translation import ugettext_lazy as _

from . managers import CustomUserManager

class CustomUser(AbstractUser):
    USER_CHOICES=(
        ('I','Individual'),
        ('S','Startup'),
    )
    username = None
    email=models.EmailField(_("Email Address"),unique=True)
    first_name = models.CharField(max_length=256,null=False,blank=False)
    middle_name=models.CharField(max_length=256)
    last_name = models.CharField(max_length=256,null=False,blank=False)
    account_type=models.CharField(max_length=1,choices=USER_CHOICES,null=False,blank=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    objects = CustomUserManager()

    def __str__(self):
        return self.email


class UserInfos(models.Model):
    Interests=(("S","Startups"),("P","Programming"),("O","Others"))
    vision=models.TextField(blank=False,null=False)
    description=models.TextField(blank=False,null=False)
    intrests=models.CharField(max_length=1,choices=Interests,blank=False,null=False)
    user=models.ForeignKey(CustomUser,on_delete=models.CASCADE)
    others=models.TextField(blank=False,null=False,default="Add Others Field...")