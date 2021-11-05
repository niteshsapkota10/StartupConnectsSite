from django.db import models

# Create your models here.
class GuestSpeaker(models.Model):
    firstname=models.CharField(max_length=256,null=False,blank=False)
    middlename=models.CharField(max_length=256,null=True,blank=True)
    lastname=models.CharField(max_length=256,null=False,blank=False)
    invited_by=models.CharField(max_length=256,null=False,blank=False)
    company=models.CharField(max_length=256,null=False,blank=False)
    status=models.IntegerField(null=False,blank=False)
    datetime=models.DateTimeField(auto_now_add=True)

class StartupMeets(models.Model):
    title=models.CharField(max_length=256,null=False,blank=False)
    datetime=models.DateTimeField()
    location=models.CharField(max_length=256,null=False,blank=False)
    venue=models.CharField(max_length=256,null=False,blank=False)
    occupancy=models.IntegerField(blank=False,null=False)
    banner=models.CharField(max_length=256,null=True,blank=True)
    theme=models.CharField(max_length=256,null=False,blank=False)
    rate=models.IntegerField(blank=False,null=False)

class GuestMeets(models.Model):
    status=models.BooleanField(default=True)
    guest=models.ForeignKey(GuestSpeaker,on_delete=models.CASCADE)
    meet=models.ForeignKey(StartupMeets,on_delete=models.CASCADE)

class StartupRegistration(models.Model):
    name=models.CharField(max_length=256,blank=False,null=False)
    email=models.EmailField(max_length=256,blank=False,null=False)
    no_of_attendes=models.IntegerField(null=False,blank=False)
    total_price=models.IntegerField(null=False,blank=False)
    is_payed=models.BooleanField(default=False)
    meet=models.ForeignKey(StartupMeets,on_delete=models.CASCADE)

class Payments(models.Model):
    registration=models.OneToOneField(StartupRegistration,on_delete=models.CASCADE)
    is_paid=models.BooleanField(default=False)

