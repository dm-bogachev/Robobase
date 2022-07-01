from django.http import HttpResponseRedirect
from database.models.Client import Client
from database.models.Robot import Robot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *


class ClientDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Client
    template_name = 'database/Client/delete.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["robots"] = Robot.objects.filter(client=self.object.pk)
        return context

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.deleted = True
        self.object.save()
        robots = Robot.objects.filter(client=self.object.pk)
        for robot in robots:
            robot.client = Client.objects.get(name="Неизвестно")
            robot.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse_lazy('client_list')

    def model_name(self):
        return self.model._meta.verbose_name
