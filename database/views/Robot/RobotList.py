from database.views import Robot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class RobotList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = Robot

    def get_queryset(self):
        qs = super().get_queryset()
        qs = Robot.objects.exclude(deleted=True)
        return qs

    def model_name(self):
        return self.model._meta.verbose_name
