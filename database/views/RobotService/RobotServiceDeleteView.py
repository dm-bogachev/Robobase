from database.models import RobotService
from database.models.Robot import Robot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *


class RobotServiceDelete(LoginRequiredMixin, DeleteView):
    login_url = 'login'
    model = RobotService
    template_name = 'database/RobotService/delete.html'

    def get_success_url(self):
        pk = self.kwargs.get('pk', None)
        robot = Robot.objects.get(robotservice=pk)
        return reverse_lazy('robot_read', kwargs={'pk': robot.pk})

    def model_name(self):
        return self.model._meta.verbose_name
