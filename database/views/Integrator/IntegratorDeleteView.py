from database.models.Integrator import Integrator
from database.models.Robot import Robot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.http import HttpResponseRedirect
from django.urls import reverse_lazy
from django.views.generic import *


class IntegratorDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Integrator
    template_name = 'database/Integrator/delete.html'

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.deleted = True
        self.object.save()
        robots = Robot.objects.filter(client=self.object.pk)
        for robot in robots:
            robot.integrator = Integrator.objects.get(name="Неизвестно")
            robot.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse_lazy('integrator_list')

    def model_name(self):
        return self.model._meta.verbose_name
