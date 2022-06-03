from database.views import Robot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *


class RobotCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Robot
    fields = '__all__'

    def __init__(self):
        super(RobotCreate, self).__init__()

    def get_success_url(self):
        return reverse_lazy('robot_list')
