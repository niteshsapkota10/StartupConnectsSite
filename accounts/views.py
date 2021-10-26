from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth import get_user_model,authenticate,login,logout
from django.contrib.auth.tokens import default_token_generator
from django.contrib.sites.shortcuts import get_current_site
from django.core.mail import EmailMessage
from django.template.loader import render_to_string
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from django.views import View
from django.views.generic import CreateView
from django.utils.decorators import method_decorator
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm,LoginForm
from .models import UserInfos
from startups.models import StartupsInfo

User=get_user_model()

class SignUpViewNormalUser(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect("/dashboard/")
        else:
            form=SignUpForm()
            return render(request,'accounts/signup.html',{
                'form':form,
                'errors':None
            })
    def post(self,request):
        form=SignUpForm(request.POST)
        print(form.data)
        if form.is_valid():
            user=form.save()
            user.is_active=False
            user.save()
            current_site=get_current_site(request)
            mail_subject='Activate Your Account'
            message=render_to_string('accounts/acc_activate_email.html',{
                'user':user,
                'domain':current_site.domain,
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),
                'token':default_token_generator.make_token(user),
            })
            to_email=form.cleaned_data.get('email')
            email=EmailMessage(mail_subject,message,to=[to_email])
            email.send()
            # return render(request, "accounts/login.html", {
            #     'form': form,
            #     'errors': form.errors,
            #     'msg': "Please Activate Your Email First . Link Sent to your provided email..",
            # })
            return redirect("/accounts/login/")
            # if user.account_type=="I":
            #     return redirect("/accounts/createuserinfo/")
            # elif user.account_type=="S":
            #     return redirect("/startups/create/")
        else:
            print(form.errors)
            return render(request, 'accounts/signup.html', {
                'form': form,
                'errors': form.errors
            })

def activate(request,uidb64,token):
    try:
        uid=urlsafe_base64_decode(uidb64).decode()
        user=User._default_manager.get(pk=uid)
    except(TypeError,ValueError,OverflowError,User.DoesNotExist):
        user=None

    if user is not None and default_token_generator.check_token(user,token):
        user.is_active=True
        user.save()
        return redirect("/accounts/login/")
    else:
        return HttpResponse("Activation Link is Invalid!!!! ")


class LoginView(View):
    def get(self,request):
        if request.user.is_authenticated:
            return redirect("/dashboard/")
        else:
            form=LoginForm()
            return render(request,"accounts/login.html",{
                'form':form,
                'errors':form.errors,
                'msg':None,
            })

    def post(self,request):
        form=LoginForm(data=request.POST)
        print(form.data)
        print(form.is_valid())
        if form.is_valid():
            email=form.cleaned_data.get('username')
            password=form.cleaned_data.get('password')
            # user=User.objects.filter(email=email,password=make_password(password=password))
            user=authenticate(request,email=email,password=password)
            # user=User.objects.get(email=email,password=password)
            print(user)
            if user is not None:
                print(user)
                login(request,user)
                return redirect("/dashboard/")
            else:
                print("User Not Found !!! ")
        else:
            print(type(form.errors))
            print(len(str((form.non_field_errors()))))
            if(len(str((form.non_field_errors())))!=140):
                return render(request, 'accounts/login.html', {
                    'form': form,
                    'errors': form.errors,
                    'msg':"Check Activation Link on your provided Email Address !!! "
                })
            else:
                return render(request, 'accounts/login.html', {
                    'form': form,
                    'errors': form.errors,
                    'msg': None
                })
        return redirect("/accounts/login/")

@method_decorator(login_required,name="dispatch")
class UserInfoCreateView(CreateView):
    model = UserInfos
    template_name = "accounts/createuserinfo.html"
    fields = ('vision','description','intrests')
    success_url = "/dashboard/"

    def dispatch(self, request, *args, **kwargs):
        user = request.user
        userInfo = UserInfos.objects.filter(user=request.user.id)
        print("UserInfo",userInfo)
        if user.account_type == 'I' and not userInfo:
            return super().dispatch(request, *args, **kwargs)
        elif user.account_type == 'S':
            startupinfo=StartupsInfo.objects.filter(user=request.user.id)
            if not startupinfo:
                return redirect("/startups/create/")
            else:
                return redirect("/dashboard/")
        else:
            return redirect("/dashboard/")

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

def dashboard(request):
    return HttpResponse("Welcome to Dashboard !!! ")

class NewActivationLink(View):
    def get(self,request):
        return render(request,"accounts/accountactivationform.html",{
            "errors":None,
        })

    def post(self,request):
        email=request.POST['email']
        try:
            user=User.objects.get(email=email)
            if user is not None:
                current_site = get_current_site(request)
                mail_subject = 'Activate Your Account'
                message = render_to_string('accounts/acc_activate_email.html', {
                    'user': user,
                    'domain': current_site.domain,
                    'uid': urlsafe_base64_encode(force_bytes(user.pk)),
                    'token': default_token_generator.make_token(user),
                })
                to_email = email
                email = EmailMessage(mail_subject, message, to=[to_email])
                email.send()
        except:
            return render(request, "accounts/accountactivationform.html", {
                "errors": "This Email Address doesnot Exists !!! ",
            })
        return redirect("/accounts/login/")

def logout_user(request):
    logout(request)
    return redirect("/accounts/login/")