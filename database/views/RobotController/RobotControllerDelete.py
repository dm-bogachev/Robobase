from django.http import HttpResponseRedirect
from database.models import RobotController
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *


class RobotControllerDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = RobotController
    template_name = 'database/base_d_form.html'

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse_lazy('robotcontroller_list')

    def model_name(self):
        return self.model._meta.verbose_name
