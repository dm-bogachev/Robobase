from database.views import Robot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *


class RobotUpdate(LoginRequiredMixin, UpdateView):
    login_url = 'login'
    model = Robot
    template_name = 'database/Robot/update.html'
    fields = '__all__'

    def get_success_url(self):
        return reverse_lazy('robot_read', kwargs={'pk': self.kwargs['pk']})

    def model_name(self):
        return self.model._meta.verbose_name
