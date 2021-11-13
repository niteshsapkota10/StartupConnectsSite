from django.db import models
from django.contrib.auth import get_user_model

User=get_user_model()
# Create your models here.
class InvestorProfile(models.Model):
    total_invested_companies=models.IntegerField(blank=False,null=False)
    is_open=models.BooleanField(default=True)
    is_verified=models.BooleanField(default=False)
    user=models.OneToOneField(User,on_delete=models.CASCADE)

class StartUpPlan(models.Model):
    problem=models.TextField(blank=False,null=False)
    solution=models.TextField(blank=False,null=False)
    mission=models.TextField(blank=False,null=False)
    category=models.CharField(max_length=256,blank=False,null=False)
    milestone=models.TextField(blank=False,null=False)
    revenue_model=models.TextField(blank=False,null=False)
    projections=models.TextField(blank=False,null=False)
    competitors=models.TextField(blank=False,null=False)
    budget=models.TextField(blank=False,null=False)
    others=models.TextField(blank=False,null=False)
    is_verified=models.BooleanField(default=False)
    user=models.ForeignKey(User,on_delete=models.CASCADE)

class InvestorFeedback(models.Model):
    feedback=models.TextField(blank=False,null=False)
    points=models.TextField(blank=False,null=False)
    decision=models.IntegerField(blank=False,null=False)
    investor=models.ForeignKey(InvestorProfile,on_delete=models.CASCADE)

