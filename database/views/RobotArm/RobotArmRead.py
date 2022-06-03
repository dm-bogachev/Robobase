from database.models import RobotArm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class RobotArmRead(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = RobotArm
    template_name = 'database/RobotArm/read.html'

    def model_name(self):
        return self.model._meta.verbose_name
