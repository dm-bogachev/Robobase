from database.views import Robot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import *


class RobotRead(LoginRequiredMixin, DetailView):
    login_url = 'login'
    model = Robot
