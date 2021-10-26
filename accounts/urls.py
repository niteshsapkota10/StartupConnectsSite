from django.urls import path
from .views import SignUpViewNormalUser,activate,LoginView,UserInfoCreateView,dashboard,NewActivationLink,logout_user

urlpatterns=[
    path('signup/',SignUpViewNormalUser.as_view()),
    path('activate/<uidb64>/<token>/',activate,name='activate'),
    path('login/',LoginView.as_view(),name="login"),
    path('createuserinfo/',UserInfoCreateView.as_view()),
    path('dashboard/',dashboard,name="dashboard"),
    path("accountactivation/",NewActivationLink.as_view()),
    path("logout/",logout_user,name='logout'),
]