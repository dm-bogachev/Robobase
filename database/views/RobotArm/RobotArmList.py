from database.models import RobotArm
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class RobotArmList(LoginRequiredMixin, ListView):
    login_url = 'login'
    model = RobotArm
    template_name = 'database/RobotArm/list.html'

    def get_queryset(self):
        qs = super().get_queryset()
        qs = RobotArm.objects.exclude(deleted=True)
        return qs

    def model_name(self):
        return self.model._meta.verbose_name
