from django.shortcuts import render,redirect,Http404
from django.contrib.auth.decorators import login_required

from accounts.models import UserInfos
from startups.models import StartupsInfo

@login_required
def dashboardHome(request):
    user=request.user
    startups = StartupsInfo.objects.all()
    if user.account_type=='I':
        try:
            userInfo=UserInfos.objects.get(user=request.user.id)
            if userInfo:
                return render(request, "dashboard/dashboard.html",{
                    "startups":startups
                })
        except:
            return redirect("/accounts/createuserinfo/")
    elif user.account_type=='S':
        startupinfo = StartupsInfo.objects.filter(user=request.user.id)
        if not startupinfo:
            return redirect("/startups/create/")
        else:
            return render(request,"dashboard/dashboard.html",{
                "startups":startups
            })
