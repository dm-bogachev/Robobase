from database.models import RobotController
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class RobotControllerRead(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = RobotController

    def model_name(self):
        return self.model._meta.verbose_name
