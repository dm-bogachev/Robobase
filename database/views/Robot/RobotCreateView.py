from django.http import request
from database.forms.Robot import RobotCreateForm
from database.views import Robot
from django.contrib.auth.mixins import LoginRequiredMixin
from django.urls import reverse_lazy
from django.views.generic import *



class RobotCreate(LoginRequiredMixin, CreateView):
    login_url = 'login'
    model = Robot
    form_class = RobotCreateForm
    # fields = ('name', 'arm_sn', 'controller_sn', 'description', 'shipping_date',
    #           'controller', 'arm', 'client', 'integrator', 'location')

    template_name = 'database/Robot/create.html'

    def __init__(self):
        super(RobotCreate, self).__init__()

    def get_success_url(self):
        return reverse_lazy('robot_list')

    def form_valid(self, form):
        form.instance.added_by = self.request.user
        return super(RobotCreate, self).form_valid(form)
