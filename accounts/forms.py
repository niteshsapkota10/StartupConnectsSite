from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from django.forms import ModelForm
from django.contrib.auth import get_user_model
from .models import UserInfos
User=get_user_model()

class SignUpForm(UserCreationForm):
    class Meta:
        model=User
        fields=('first_name','last_name','email','password1','password2','account_type')

class LoginForm(AuthenticationForm):
    class Meta:
        model=User
        fields=('email','password')


