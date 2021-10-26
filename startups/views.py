from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import CreateView,ListView,UpdateView,DeleteView
from .models import StartupsInfo
from django.forms.widgets import SelectDateWidget
@method_decorator(login_required,name='dispatch')
class CreateStartUpView(CreateView):
    model = StartupsInfo
    template_name = "startups/createstartup.html"
    fields = ('startupname','category','description','vision','startedDate','location','phone_number','phone_number2')
    success_url = "/startups/list/"

    def get_form(self):
        '''add date picker in forms'''
        form = super(CreateView, self).get_form()
        form.fields['startedDate'].widget =SelectDateWidget()
        return form

    def form_valid(self, form):
        form.instance.user=self.request.user
        return super().form_valid(form)

@method_decorator(login_required,name='dispatch')
class ListStartupView(ListView):
    model = StartupsInfo
    paginate_by = 10
    template_name = "startups/liststartups.html"

@method_decorator(login_required,name='dispatch')
class DetailStartupView(DeleteView):
    model = StartupsInfo
    template_name = "startups/detailstartup.html"

@method_decorator(login_required,name='dispatch')
class UpdateStartupView(UpdateView):
    model = StartupsInfo
    template_name = "startups/updatestartup.html"
    fields = '__all__'
    success_url = "/startups/list/"

@method_decorator(login_required,name='dispatch')
class DeleteStartup(DeleteView):
    model = StartupsInfo
    success_url = "/startups/list/"
    template_name = "startups/deletestartup.html"
