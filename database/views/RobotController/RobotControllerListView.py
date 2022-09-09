from database.models import RobotController
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class RobotControllerList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = RobotController
    template_name = 'database/RobotController/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = RobotController.objects.exclude(deleted=True)
        return qs

    def model_name(self):
        return self.model._meta.verbose_name
