from database.models import Client, Integrator, Robot
from database.models.Location import Location
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *
from django.http import HttpResponseRedirect

class LocationDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = Location
    template_name = 'database/Location/delete.html'

    def form_valid(self, form):
        success_url = self.get_success_url()
        self.object.deleted = True
        self.object.save()
        robots = Robot.objects.filter(location=self.object.pk)
        for robot in robots:
            robot.location = Location.objects.get(country="Неизвестно")
            robot.save()
        clients = Client.objects.filter(location=self.object.pk)
        for client in clients:
            client.location = Location.objects.get(country="Неизвестно")
            client.save()
        integrators = Integrator.objects.filter(location=self.object.pk)
        for integrator in integrators:
            integrator.location = Location.objects.get(country="Неизвестно")
            integrator.save()
        return HttpResponseRedirect(success_url)

    def get_success_url(self):
        return reverse_lazy('location_list')

    def model_name(self):
        return self.model._meta.verbose_name
