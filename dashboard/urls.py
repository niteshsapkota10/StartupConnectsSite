from django.urls import path
from .views import dashboardHome

urlpatterns=[
    path("",dashboardHome),
]