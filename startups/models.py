from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
from members.models import Ceos

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
    problem=models.TextField(blank=False,null=False)
    logo=models.CharField(max_length=256,null=False,blank=False)
    banner=models.CharField(max_length=256,null=True,blank=True)
    primary_color=models.CharField(max_length=50,null=False,blank=False)
    secondary_color=models.CharField(max_length=50,null=True,blank=True)
    ceo=models.OneToOneField(Ceos,on_delete=models.CASCADE)
    startup_quote=models.CharField(max_length=555,null=False,blank=True)
    is_verified=models.BooleanField(default=False)

    def __str__(self):
        return self.startupname

class Favourites(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    startup=models.ForeignKey(StartupsInfo,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

class StartupsContactInfo(models.Model):
    email=models.EmailField(max_length=256,blank=False,null=False)
    email2=models.EmailField(max_length=256,blank=True,null=True)
    website=models.CharField(max_length=256,blank=False,null=False)
    location=models.CharField(max_length=256,blank=False,null=False)
    fb_page=models.CharField(max_length=550,blank=True,null=True)
    ig_ac=models.CharField(max_length=550,blank=True,null=True)
    linkedin_ac=models.CharField(max_length=550,blank=True,null=True)
    twitter_ac=models.CharField(max_length=550,blank=True,null=True)
    startup=models.OneToOneField(StartupsInfo,on_delete=models.CASCADE)

class StartupTeams(models.Model):
    first_name=models.CharField(max_length=256,blank=False,null=False)
    last_name=models.CharField(max_length=256,blank=False,null=False)
    position=models.CharField(max_length=256,blank=False,null=False)
    email=models.EmailField(max_length=256,blank=False,null=False)
    phone_no=models.CharField(max_length=256,blank=False,null=False)
    photo=models.CharField(max_length=256,blank=False,null=False)
    roles=models.TextField(blank=False,null=False)
    if_exists=models.BooleanField(default=False)
    is_verified=models.BooleanField(default=False)
    startup=models.ForeignKey(StartupsInfo,on_delete=models.CASCADE)

class StartupViews(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    startup=models.OneToOneField(StartupsInfo,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)

class StartupClaps(models.Model):
    user=models.OneToOneField(User,on_delete=models.CASCADE)
    startup=models.OneToOneField(StartupsInfo,on_delete=models.CASCADE)
    status=models.BooleanField(default=False)
