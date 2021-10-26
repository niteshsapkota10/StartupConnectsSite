from django.urls import path
from .views import CreateStartUpView,ListStartupView,DetailStartupView,UpdateStartupView,DeleteStartup

urlpatterns=[
    path("create/",CreateStartUpView.as_view()),
    path("list/",ListStartupView.as_view()),
    path("detail/<pk>/",DetailStartupView.as_view()),
    path("update/<pk>/",UpdateStartupView.as_view()),
    path("delete/<pk>/",DeleteStartup.as_view()),
]