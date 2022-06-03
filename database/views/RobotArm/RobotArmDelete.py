from django.http import HttpResponseRedirect
from database.models import RobotArm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *


class RobotArmDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = RobotArm
    template_name = 'database/RobotArm/delete.html'

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.deleted = True
        self.object.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse_lazy('robotarm_list')

    def model_name(self):
        return self.model._meta.verbose_name
